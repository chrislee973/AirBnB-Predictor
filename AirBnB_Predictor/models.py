from flask_sqlalchemy import SQLAlchemy



DB = SQLAlchemy()
features = ['property_type', 'room_type', 'amenities', 'accommodates', 'bathrooms', 'bed_type', 'cancellation_policy', 'cleaning_fee', 'city', 
                'description', 'host_has_profile_pic', 'host_identity_verified', 'instant_bookable', 'name', 'number_of_reviews', 'bedrooms', 'beds']


class Listing(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    listing_name = DB.Column(DB.String)
    city = DB.Column(DB.String(25))
    zipcode = DB.Column(DB.Float, nullable=False)

    def __repr__(self):        
        return f"Name: {self.listing_name} --- City: {self.city}"


def add_new_listing(listing_name, city, zipcode):
    """Add or update a user listing."""
    #Get listing if it exists. If not, make new listing
    #listing = (Listing.query.get(Listing.listing_name) or Listing(listing_name=listing_name, city=city, zipcode=zipcode))

    #No checking if it's an existing query (for now, since it's generating errors). Just make a new listing
    listing =  Listing(listing_name=listing_name, city=city, zipcode=zipcode)

    DB.session.add(listing)
    DB.session.commit()
    
