from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

features = ["property_type", "room_type", "amenities", "accommodates", "bathrooms", "bed_type", "cancellation_policy", "cleaning_fee", "city", 
                "description", "host_has_profile_pic", "host_identity_verified", 
                "instant_bookable", "listing_name", "number_of_reviews", "bedrooms", "beds", "listing_name", "zipcode"]

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
    zipcode = DB.Column(DB.BigInteger)
    number_of_reviews = DB.Column(DB.Integer)
    bedrooms = DB.Column(DB.Integer)
    beds = DB.Column(DB.Integer)

    def __repr__(self):        
        return f"Name: {self.listing_name} --- City: {self.city}"

def add_update_listing(property_type, room_type, amenities, accommodates, bathrooms, bed_type, cancellation_policy, cleaning_fee, city,
                    description, host_has_profile_pic, host_identity_verified, instant_bookable, 
                    number_of_reviews, bedrooms, beds, name, zipcode):
    """Add or update a user listing."""
    #Get listing if it exists. If not, make new listing
    listing = Listing.query.filter_by(listing_name=name).first()

    if listing is None:
        listing =  Listing(property_type=property_type, room_type=room_type, amenities=amenities, accommodates=accommodates, bathrooms=bathrooms, 
                        bed_type=bed_type, cancellation_policy=cancellation_policy, cleaning_fee=cleaning_fee, city=city,
                    description=description, host_has_profile_pic=host_has_profile_pic, host_identity_verified=host_identity_verified, 
                    instant_bookable=instant_bookable, number_of_reviews=number_of_reviews, bedrooms=bedrooms, 
                    beds=beds, listing_name=name, zipcode=zipcode)
        DB.session.add(listing)
    else:
        listing.property_type = property_type
        listing.room_type = room_type
        listing.amenities = amenities
        listing.accommodates = accommodates
        listing.bathrooms = bathrooms
        listing.bed_type = bed_type
        listing.cancellation_policy = cancellation_policy
        listing.cleaning_fee = cleaning_fee
        listing.city = city
        listing.description = description
        listing.host_has_profile_pic = host_has_profile_pic
        listing.host_identity_verified = host_identity_verified
        listing.instant_bookable = instant_bookable
        listing.zipcode = zipcode
        listing.number_of_reviews = number_of_reviews
        listing.bedrooms = bedrooms
        listing.beds = beds
    
    DB.session.commit()