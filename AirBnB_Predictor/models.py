from flask_sqlalchemy import SQLAlchemy



DB = SQLAlchemy()

features = ['property_type', 'room_type', 'amenities', 'accommodates', 'bathrooms', 'bed_type', 'cancellation_policy', 'cleaning_fee', 'city', 
                'description', 'host_has_profile_pic', 'host_identity_verified', 
                'instant_bookable', 'number_of_reviews', 'bedrooms', 'beds', 'listing_name', 'zipcode']


class Listing(DB.Model): 
    id = DB.Column(DB.Integer, primary_key=True)
    property_type = DB.Column(DB.String)
    room_type = DB.Column(DB.String)
    amenities = DB.Column(DB.String)
    accommodates = DB.Column(DB.Integer)
    bathrooms = DB.Column(DB.Float)
    bed_type = DB.Column(DB.String)
    cancellation_policy = DB.Column(DB.String)
    cleaning_fee = DB.Column(DB.String)
    city = DB.Column(DB.String)
    description = DB.Column(DB.String)
    host_has_profile_pic = DB.Column(DB.String)
    host_identity_verified = DB.Column(DB.String)
    instant_bookable = DB.Column(DB.String)
    listing_name = DB.Column(DB.String)
    zipcode = DB.Column(DB.Float)
    number_of_reviews = DB.Column(DB.Integer)
    bedrooms = DB.Column(DB.Integer)
    beds = DB.Column(DB.Integer)

    def __repr__(self):        
        return f"Name: {self.listing_name} --- City: {self.city}"


def add_new_listing(property_type, room_type, amenities, accommodates, bathrooms, bed_type, cancellation_policy, cleaning_fee, city,
                    description, host_has_profile_pic, host_identity_verified, instant_bookable, 
                    number_of_reviews, bedrooms, beds, listing_name, zipcode):
    """Add or update a user listing."""
    #Get listing if it exists. If not, make new listing
    #listing = (Listing.query.get(Listing.listing_name) or Listing(listing_name=listing_name, city=city, zipcode=zipcode))

    #No checking if it's an existing query (for now, since it's generating errors). Just make a new listing
    listing =  Listing(property_type=property_type, room_type=room_type, amenities=amenities, accommodates=accommodates, bathrooms=bathrooms, 
                        bed_type=bed_type, cancellation_policy=cancellation_policy, cleaning_fee=cleaning_fee, city=city,
                    description=description, host_has_profile_pic=host_has_profile_pic, host_identity_verified=host_identity_verified, 
                    instant_bookable=instant_bookable, number_of_reviews=number_of_reviews, bedrooms=bedrooms, 
                    beds=beds, listing_name=listing_name, zipcode=zipcode)

    DB.session.add(listing)
    DB.session.commit()
    

