from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

features = ['property_type', 'room_type', 'amenities', 'accommodates', 'bathrooms', 'bed_type', 'cancellation_policy', 'cleaning_fee', 'city', 
                'description', 'host_has_profile_pic', 'host_identity_verified', 'instant_bookable', 'name', 'number_of_reviews', 'bedrooms', 'beds']


class Listing(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    listing_name = DB.Column(DB.String)
    city = DB.Column(DB.String(25))
    zipcode = DB.Column(DB.BigInteger, nullable=False)

    def __repr__(self):        
        return f"Name: {self.listing_name} --- City: {self.city}"

def add_new_listing(name, city, zipcode):
    """Add or update a user listing."""
    #Get listing if it exists. If not, make new listing
    listing = Listing.query.filter_by(listing_name=name).first()

    if listing is None:
        listing =  Listing(listing_name=name, city=city, zipcode=zipcode)
        DB.session.add(listing)
    else:
        listing.city = city
        listing.zipcode = zipcode
    
    DB.session.commit()