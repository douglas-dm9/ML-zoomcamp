
#### ML Zoomcamp Mid Term Project by Douglas Melo

Dataset: https://github.com/americanas-tech/b2w-reviews01

B2W-Reviews01 is an open corpus of product reviews in portuguese. It contains more than 130k e-commerce customer reviews, collected from the Americanas.com website between January and May, 2018. B2W-Reviews01 offers rich information about the reviewer profile, such as gender, age, and geographical location. The corpus also has two different review rates:

The usual 5-point scale rate, represented by stars in most e-commerce websites,
a "recommend to a friend" label, a "yes or no" question representing the willingness of the customer to recommend the product to someone else.

The ideia here is this project is to build a model to predict if a review has a positive, negative or neutral sentiment and deploy the model using BentoML and Docker to deploy on the AWS Cloud using. This service can be used improve company comunications with their customers and give a better feeling of what your customers are talking about your product or service. There are no much projects for sentiment analysis in portuguese, so this project aims to help in this context.

 [Link to the service deployed on the AWS Elastic Container Service](http://18.231.113.77:3000)

Unfurtunately, I had do drop my cluster in AWS because the billing costs. So I'll show bellow some examples in the swagger UI of the model.

![image](https://user-images.githubusercontent.com/58889801/201478236-e56f1139-324f-42a9-94a3-ecba70aae007.png)

Example: Negative comment:
![image](https://user-images.githubusercontent.com/58889801/201478270-6c2cbdf5-21ae-47d3-a1dc-4fa33e4db462.png)

Example: Positive comment:
![image](https://user-images.githubusercontent.com/58889801/201478409-4e313150-9ade-4aac-9431-634da857ff9d.png)


Example: Neutral comment:
![image](https://user-images.githubusercontent.com/58889801/201478453-fd33bcad-361b-4019-bb1f-854707b6b91f.png)
