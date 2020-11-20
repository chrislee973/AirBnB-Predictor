# AirBnB Predictor

### An application to predict the price of AirBnb lisings.

It can be a fine art trying to decide what price to set for your AirBnB listing. You want to set a price hight enough to return some profit but not too high to send people to your competition.

Big corporations and businesses taking advantage of the tourism market with multiple listings may not need to deal with this. On the other hand, there are a lot of local mom-and-pop listers grappling with this catch-22. Several blogs and articles exist online on possible best practices and criteria to consider before setting a price.

At AirBnB Predictor, we aim to give you peace of mind on the pricing front by revealing the optimal price for your listing. Our model considers the various features of your listing and tells you what the optimal listing price should be, allowing yout to focus your efforts elsewhere.

Renters can also use our app to have an idea of the optimal listing price to search for with the features they'd like to have.

Some of the services our app provides:

* Determines optimal price for different property types in five major cities: Boston, new York, LA, Washington, Chicago, and San Francisco.
* Save multiple properties and see them in my listings.
* Click on any listing name to see all the features of that particular listing.
* Made a mistake or changed a feature? Customize saved features and see how it affects optimal price with Adjust Settings.
* Amenities are important! Be sure to list all your amenities to get a more accurate result.

Check out [our app](https://airbnbpredictor.herokuapp.com/) today and let us help you create your best listing!

## For the technical savvy

We used a keras model to perform NLP on the Description and Amenities features. Our app takes both inputs and runs it through the BOW and sequence embedding functions before passing it to the model. We performed ordinal encoding on the categorical columns making everything numerical before passing into the model. Check out the notebook for the steps taken.


### Data
Data gotten from Kaggle: [AirBnB Listings in Major US Cities](https://www.kaggle.com/rudymizrahi/airbnb-listings-in-major-us-cities-deloitte-ml?select=train.csv)



Brought to you by James Haggerman, Reid Harris, Christopher Lee, and Ik Okoro
