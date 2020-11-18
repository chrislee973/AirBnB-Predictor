from flask import Flask, render_template, request
from .models import Listing, DB, add_new_listing, features
from .predict import predict_rate


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)
    #DB.create_all()


    #Home page
    @app.route('/', methods = ['POST', 'GET'])
    def root():
        return render_template('test.html', title='Home')
    

    @app.route('/add_listing', methods=['POST', 'GET'])
    def add_listing():
        
        add_new_listing(property_type= request.values['property_type'], room_type= request.values['room_type'], amenities= request.values['amenities'], 
            accommodates= request.values['accommodates'], bathrooms=request.values['bathrooms'], bed_type= request.values['bed_type'], 
            cancellation_policy= request.values['cancellation_policy'], cleaning_fee= request.values['cleaning_fee'], city=request.values['city'], 
                description= request.values['description'], host_has_profile_pic= request.values['host_has_profile_pic'], host_identity_verified= request.values['host_identity_verified'], 
                instant_bookable=request.values['instant_bookable'], number_of_reviews= request.values['number_of_reviews'], 
            bedrooms= request.values['bedrooms'], beds= request.values['beds'], listing_name= request.values['listing_name'], zipcode= request.values['zipcode'])
                
        #Display listing status message
        add_listing_status_message = "Listing successfully added!"

        return render_template('test.html', title='Home', listings=Listing.query.all(), add_listing_status_message=add_listing_status_message)       
        #return request.values['city']


    #When user clicks "Predict rate" button
    @app.route('/predict', methods=['POST', 'GET'])
    def predict():
        prediction = predict_rate()
        #prediction = 213
        #predict_message = f"Your optimal nightly rate is ${prediction}."
        #return render_template('test.html', title='Home', predict_message=predict_message)
        return str(prediction)


    #When user clicks "+ New listing" button
    @app.route('/new_listing')
    def new_listing():
        return render_template("test.html")


    #When user clicks "My listings" button
    @app.route('/listings')
    def listings():
        return render_template('listings.html', title='listings', listings=Listing.query.all())


    #Resets the database (for development troubleshooting purposes only. Take this out when deploying)
    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('test.html', title='Reset database!')


    #When "Adjust settings" is clicked from the user's listings page
    @app.route('/adjust_listing/<listing_name>', methods=['GET'])
    def adjust_listing(listing_name=None):
        listing_name=listing_name or request.values['listing_name']
        listing= Listing.query.filter(Listing.listing_name == listing_name).one()
        return render_template('adjust_listing.html', title='Tweak listings', listing_name=listing.listing_name, zipcode=listing.zipcode)
        #return str(listing.accommodates)

    return app
