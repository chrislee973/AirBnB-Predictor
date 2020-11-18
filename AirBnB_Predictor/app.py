from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from .models import Listing, DB, add_update_listing


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)

    #Home page
    @app.route('/', methods = ['POST', 'GET'])
    def root():
        DB.create_all()
        return render_template("test.html", title="Home", listings=Listing.query.all())
    

    @app.route('/add_listing', methods=['POST', 'GET'])
    def add_listing():
        #When user clicks on "Add listing" button
        add_update_listing(property_type= request.values["property_type"], room_type= request.values["room_type"], amenities= request.values["amenities"], 
            accommodates= request.values["accommodates"], bathrooms=request.values["bathrooms"], bed_type= request.values["bed_type"], 
            cancellation_policy= request.values["cancellation_policy"], cleaning_fee= request.values["cleaning_fee"], city=request.values["city"], 
                description= request.values["description"], host_has_profile_pic= request.values["host_has_profile_pic"], host_identity_verified= request.values["host_identity_verified"], 
                instant_bookable=request.values["instant_bookable"], number_of_reviews= request.values["number_of_reviews"], 
            bedrooms= request.values["bedrooms"], beds= request.values["beds"], listing_name= request.values["listing_name"], zipcode= request.values["zipcode"])

        #Display status message
        add_listing_status_message = "Listing successfully added!"
        return render_template("test.html", title="Home", listings=Listing.query.all(), add_listing_status_message = add_listing_status_message)       


    #When user clicks "Predict rate" button
    @app.route('/predict')
    def predict():
        #prediction = predict_rate(listing_name)
        prediction = 213
        predict_message = f"Your optimal nightly rate is ${prediction}."
        return render_template('test.html', title='Home', predict_message=predict_message)


    #When user clicks "+ New listing" button
    @app.route('/new_listing')
    def new_listing():
        return render_template("test.html")


    #When user clicks "My listings" button
    @app.route('/listings')
    def listings():
        return render_template("listings.html", title="listings", listings=Listing.query.all())


    #Resets the database (for development troubleshooting purposes only. Take this out when deploying)
    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template("test.html", title="Reset database!")


    #When "Adjust settings" is clicked from the user's listings page
    # View populated fields
    @app.route('/adjust_listing/<listing_name>', methods=['GET'])
    def adjust_listing(listing_name=None):
        listing_name=listing_name or request.values['listing_name']

        cities = ["New York City", "Los Angeles", "Washington DC", "Chicago"]
        properties = ["Apartment", "Bed & Breakfast", "Bungalow", "Condominium", "Guest House", 
                    "Hostel", "House", "Loft", "Townhouse", "Other"]
        rooms = ["Entire House/apt", "Private room", "Shared room"]
        beds = ["Real bed", "Futon", "Pull-out sofa", "Airbed", "Couch"]
        cleaning = ["Yes", "No"]
        pic = ["Yes", "No"]
        verified = ["Yes", "No"]
        instant = ["Yes", "No"]
        cancellation = ["Flexible", "Moderate", "Strict", "Super strict - 30", "Super strict - 60"]

        listing= Listing.query.filter(Listing.listing_name == listing_name).one()
        return render_template("adjust_listing.html", title="Tweak listings", listing_name=listing_name, listing=listing, 
                                all_cities=cities, property_types = properties, bed_types = beds, cleaning_types = cleaning,
                                pic_types = pic, verified_types = verified, instant_types = instant, cancellation_types = cancellation)

    @app.route('/listings/<listing_name>')
    def list_features(listing_name=None):
        listing_name = listing_name or request.values["listing_name"]
        listing = Listing.query.filter(Listing.listing_name == listing_name).one()
        return render_template("listing_features.html", title=f"{listing_name}'s Features", listing_name=listing_name, listing=listing)
    
    @app.route('/about')
    def aboout():
        return render_template("about.html")
    
        
    return app