import pickle
from flask import request
import keras


#model = pickle.load(open("model.p", "rb"))
#model = keras.models.load_model('AirBnB_Predictor/Keras_model')


def bow(text):
    """Function to convert description and amenities features into bow"""
    vocab_size = 10000
    tokenize = keras.preprocessing.text.Tokenizer(num_words=10000, char_level = False)
    tokenize.fit_on_texts(text)
    bow = tokenize.texts_to_matrix(text)
    return bow


def seq_embed(text):
    """Function to convert description and amenities features into embeddings"""
    tokenize = keras.preprocessing.text.Tokenizer(num_words=10000, char_level = False)
    tokenize.fit_on_texts(text)
    seq = tokenize.texts_to_sequences(seq)
    max_seq_length = 170
    seq = keras.preprocessing.sequence.pad_sequences(
    seq, maxlen = max_seq_length, padding = 'post')
    return seq


def predict_rate():
    """
    
    Grabs form data for each feature that the model takes and then
    appends all the feature data for that particular listing into a list called "feature_list", which is then fed into the model.
    
    Example feature list: ['House', 'Shared room', 'Cable TV, Wireless internet, free parking', '5', '3.0', 'Real bed', 
                            'Flexible', 'Yes', 'Los Angeles', 'Gentle breeze, awesome views', 'No', 'Yes', 'Yes', '50', '4', '3']

    Example feature_dict: {'property_type': 'House', 'room_type': 'Shared room', 'amenities': 'Cable TV, Wireless internet, free parking', 
                            'accommodates': '5', 'bathrooms': '3.0', 'bed_type': 'Real bed', 'cancellation_policy': 'Flexible', 
                            'cleaning_fee': 'Yes', 'city': 'Los Angeles', 'description': 'Gentle breeze, awesome views', 
                            'host_has_profile_pic': 'No', 'host_identity_verified': 'Yes', 'instant_bookable': 'Yes', 
                            'number_of_reviews': '50', 'bedrooms': '4', 'beds': '3'}
    Example output: 213
    """
    
    features = ['property_type', 'room_type', 'amenities', 'accommodates', 'bathrooms', 'bed_type', 'cancellation_policy', 'cleaning_fee', 'city', 
                'description', 'host_has_profile_pic', 'host_identity_verified', 
                'instant_bookable', 'number_of_reviews', 'bedrooms', 'beds']

    feature_dict = {}
    for f in features:
        #feature_list.append(request.values[f])
        feature_dict[f] = request.values[f]
    
    #Bag of words representation of descsription feature
    desc_bow = bow(feature_dict['description'])

    #Bag of words representation of amenities feature
    amenities_bow = bow(feature_dict['amenities'])

    #Embedding of description
    desc_embed = seq_embed(feature_dict['description'])

    #Embedding of amenities
    amenities_embed = seq_embed(feature_dict['amenities'])

    return (desc_bow, amenities_bow)

if __name__ == "__main__":
    print(model)