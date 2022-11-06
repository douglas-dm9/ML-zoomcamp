
#### ML Zoomcamp Capstone Project by Douglas Melo

Dataset: https://github.com/americanas-tech/b2w-reviews01

B2W-Reviews01 is an open corpus of product reviews in portuguese. It contains more than 130k e-commerce customer reviews, collected from the Americanas.com website between January and May, 2018. B2W-Reviews01 offers rich information about the reviewer profile, such as gender, age, and geographical location. The corpus also has two different review rates:

the usual 5-point scale rate, represented by stars in most e-commerce websites,
a "recommend to a friend" label, a "yes or no" question representing the willingness of the customer to recommend the product to someone else.

The ideia here is this project is to build a model to predict if a review has a positive, negative or neutral sentiment and deploy the model using BentoML and Docker to deploy on the AWS Cloud using.

 [Link to the service deployed on the AWS Elastic Container Service](http://18.228.7.125:3000/#/)
 
Unfortunately I didn't manage to make the service return a response status 200 because I'm using some packages from the nltk library (stopwords and punkt) and I don't know yet how to make this available on my bento , but i' m working on the solution. Besides that , i could not export the dockerfile , because i'm using WSL2 on my company machine and don't have access to the Linux files.
 
  Because the deadline for the project is tomorrow , i decide to deploy the service , even if it's not work yet . There is a print bellow showing the service running on my local machine.

![image](https://user-images.githubusercontent.com/58889801/200193432-334f0f2f-6a23-4928-81cb-4dbd595ccfdf.png)

