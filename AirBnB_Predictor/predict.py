import pickle

#model = pickle.load(open("model.p", "rb"))

def predict_rate():
    """
    Takes in a list of features and predicts the optimal nightly rate (in $)

    Example input: ['Apartment', 'Private Room', ['TV', 'Wireless Internet'], ..., 3, 4]
    Example output: 213
    """
    
    features = ['property_type', 'room_type', 'amenities', 'accommodates', 'bathrooms', 'bed_type', 'cancellation_policy', 'cleaning_fee', 'city', 
                'description', 'host_has_profile_pic', 'host_identity_verified', 
                'instant_bookable', 'listing_name', 'number_of_reviews', 'bedrooms', 'beds', 'listing_name', 'zipcode']

    feature_list = []
    for f in features:
        feature_list.append(request.values[f])
    
    
    #return model.predict(feature_list)
    return feature_list