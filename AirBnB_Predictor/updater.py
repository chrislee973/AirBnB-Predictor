from.DB_test import DB, Listings

def add_listing(list_name, list_city, list_zip, list_description, list_amenities):
    db_listing = Listings(name = list_name, city = list_city, zipcode = list_zip, description = list_description, amenities = list_amenities)
    DB.session.add(db_listing)
    DB.session.commit()