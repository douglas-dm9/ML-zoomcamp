import bentoml
from bentoml.io import JSON
from bentoml.io import Text


bento_model = bentoml.sklearn.get("sentiment_analysis_pipeline:latest")
pre_processor = bento_model.custom_objects["pre_processor"]
stop_words = bento_model.custom_objects["stop_words"]
get_sentiment = bento_model.custom_objects["get_sentiment"]
model_runner = bento_model.to_runner()


svc = bentoml.Service("sentiment_classifier", runners=[model_runner])


#@svc.api(input=Text(), output=JSON())
#async def predict(input_doc: str):
#    predictions = await model_runner.predict.async_run([input_doc])
#    return {"result": predictions[0]}


@svc.api(input=Text(), output=JSON())
async def predict(input_doc: str):
    predictions = await model_runner.predict_proba.async_run([pre_processor(input_doc)])
    return get_sentiment(predictions[0][0])
# Test running inference with BentoML runner

#test_runner = bento_model.to_runner()
#test_runner.init_local()
#print(get_sentiment(test_runner.predict_proba.run(["hello"])[0][0])) 