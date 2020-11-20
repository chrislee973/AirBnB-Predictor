# AirBnB Predictor

### An application to predict the price of AirBnb lisings.

As a host, it can be a fine art trying to decide what price to set for your AirBnB listing. It's hard to get a sense of a competitive market rate for listings with features similar to yours. You want to set a price high enough to return some profit but not too high to send people to your competition.

Big corporations and businesses with hundreds or even thousands of listings may not need to deal with this. On the other hand, independent mom-and-pop hosts like yourself have to grapple with this catch-22.

At AirBnB Predictor, we aim to give you peace of mind on the pricing front by suggesting the optimal price for your listing. Our machine learning model considers the various features of your listing and tells you what the optimal nightly rate should be, allowing you to focus your efforts elsewhere.

Renters can also use our app to get an idea of the rates they should expect to see for listings with the specific features they have in mind.

Some of the services our app provides:

* Determines optimal price for different property types in five major cities: Boston, new York, LA, Washington, Chicago, and San Francisco.
* Own multiple listings? Save and manage all your listings in the "My listings" page.
* Click on any listing name to see all the features of that particular listing.
* Made a mistake? Curious about how changing a certain feature of your listing will affect the optimal rate? Customize saved features and see how it affects optimal price.
* Amenities are important! Be sure to list all your amenities to get a more accurate result.

Check out [our app](https://airbnbpredictor.herokuapp.com/) today and let us help you create your best listing!

## Machine Learning pipeline

Because Airbnb listing information contains a mixture of categorical and text data(like the description of the listing), we made a Keras model that can take in and make predictions on both text and numerical/categorical data. Because our model is required to work with multiple data types, we ran the text and categorical data through separate preprocessing pipelines. First, we took the Description and Amenities feataures and fed them through the BOW and sequence embedding functions before finally passing it to the model. We then performed ordinal encoding on the categorical feaetures before passing those into the model. Check out the notebook for the exact steps taken.


### Data
Data gotten from Kaggle: [AirBnB Listings in Major US Cities](https://www.kaggle.com/rudymizrahi/airbnb-listings-in-major-us-cities-deloitte-ml?select=train.csv)



Brought to you by James Haggerman, Reid Harris, Christopher Lee, and Ik Okoro
