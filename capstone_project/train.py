from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
import pandas as pd
import unidecode
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
import bentoml

df= pd.read_csv(r"https://github.com/americanas-tech/b2w-reviews01/raw/main/B2W-Reviews01.csv",delimiter=",",encoding='utf-8')
df = df[['review_text','overall_rating']]
df = df.drop(df[df.overall_rating == 3].index)
df['overall_rating'].replace([1,2], 0, inplace=True)
df['overall_rating'].replace([4,5], 1,inplace=True)
df_reviews_positive = df[df['overall_rating'] == 1].sample(n=35758,random_state=42)
df_reviews_negative = df[df['overall_rating'] == 0]
df = pd.concat([df_reviews_positive,df_reviews_negative], ignore_index=True)
df.rename(columns={'review_text':'text','overall_rating':'labels'},inplace=True)

df['text'] = df['text'].str.replace('\d+', '').astype(str)

stop_words = set(stopwords.words('portuguese'))
stop_words.remove('não')

def pre_processor(text):
  text = text.lower()
  tokenized = word_tokenize(text)
  filtered_sentence = [unidecode.unidecode(word) for word in tokenized if word not in stop_words ]
  return ' '.join(c for c in filtered_sentence if c.isalpha())

df.text = df.text.apply(pre_processor)

train, test = train_test_split(df, test_size = 0.3, stratify = df['labels'], random_state = 42)

X_train=train['text'].values
y_train = train['labels'].values


pipeline= Pipeline([('tf', TfidfVectorizer(max_features=1000,  ngram_range = (1,2))),
                     ('clf', LogisticRegression(solver = 'liblinear', random_state = 42))])


parameters  = {
               'clf__penalty': ['l1', 'l2'],
               'clf__C': [1.0, 10.0, 100.0]
             }

gs_lr_tfidf = GridSearchCV(pipeline, parameters , scoring='accuracy',
                           cv=5, verbose=1, n_jobs=-1)

gs_lr_tfidf.fit(X_train, y_train) 

best_parameters = gs_lr_tfidf.best_estimator_.get_params()
best_parameters = {
    param_name: best_parameters[param_name] for param_name in sorted(parameters.keys())
}

def get_sentiment(prob):
    if prob >= 0.60:
        return 'Negative'
    elif prob <= 0.30:
        return 'Positive'
    else:
        return 'Neutral'


bento_model = bentoml.sklearn.save_model(
    "sentiment_analysis_pipeline",
    gs_lr_tfidf.best_estimator_,
    signatures={
        "predict": {"batchable": True, "batch_dim": 0},
        "predict_proba": {"batchable": True, "batch_dim": 0},
    },
    custom_objects={
        "pre_processor": pre_processor,
        "get_sentiment": get_sentiment,
        "stop_words": stop_words
    },
     metadata=best_parameters,
)

print(f"Model saved: {bento_model}")

test_runner = bentoml.sklearn.get("sentiment_analysis_pipeline:latest").to_runner()
test_runner.init_local()
print(test_runner.predict.run(["hello"]))