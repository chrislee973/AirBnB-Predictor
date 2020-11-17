import pickle

model = pickle.load(open("model.p", "rb"))

def predict_rate(listing_name):
    """
    Takes in a list of features and predicts the optimal nightly rate (in $)

    Example input: ['Apartment', 'Private Room', ['TV', 'Wireless Internet'], ..., 3, 4]
    Example output: 213
    """
    
    listing = Listing.query.filter(Listing.name == listing_name).one()
    features = ['property_type', 'room_type', 'amenities', 'accommodates', 'bathrooms', 'bed_type', 'cancellation_policy', 'cleaning_fee', 'city', 
                'description', 'host_has_profile_pic', 'host_identity_verified', 'instant_bookable', 'name', 'number_of_reviews', 'bedrooms', 'beds']

    feature_list = []
    for f in features:
        feature_list.append(listing.f)
    
    return model.predict(feature_list)
