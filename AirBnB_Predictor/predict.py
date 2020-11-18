import pickle
from flask import request
#model = pickle.load(open("model.p", "rb"))

def predict_rate():
    """
    
    Grabs form data for each feature that the model takes and then
    appends all the feature data for that particular listing into a list called "feature_list", which is then fed into the model.
    
    Example feature_list: ['Apartment', 'Private Room', ['TV', 'Wireless Internet'], ..., 91007 ]
    Example output: 213
    """
    
    features = ['property_type', 'room_type', 'amenities', 'accommodates', 'bathrooms', 'bed_type', 'cancellation_policy', 'cleaning_fee', 'city', 
                'description', 'host_has_profile_pic', 'host_identity_verified', 
                'instant_bookable', 'number_of_reviews', 'bedrooms', 'beds', 'listing_name', 'zipcode']

    feature_list = []
    for f in features:
        feature_list.append(request.values[f])
    
    
    #return model.predict(feature_list)
    return feature_list