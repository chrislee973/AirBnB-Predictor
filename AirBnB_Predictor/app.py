from flask import Flask, render_template, request
from .models import Listing, DB, add_new_listing
#from .predict import predict_rate


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)
    #DB.create_all()

    #Home page
    @app.route('/', methods = ['POST', 'GET'])
    def root():
        #DB.create_all()
        return render_template('test.html', title='Home', listings=Listing.query.all())
    

    @app.route('/add_listing', methods=['POST', 'GET'])
    def add_listing():
        #When user clicks on "Add listing" button
        add_new_listing(request.values["listing_name"], request.values["city"], request.values["zipcode"])

        #Display status message
        add_listing_status_message = "Listing successfully added!"
        return render_template('test.html', title='Home', listings=Listing.query.all(), add_listing_status_message = add_listing_status_message)       


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
        #listing= Listing.query.filter(Listing.listing_name == list_name).one()
        return render_template('adjust_listing.html', title='Tweak listings', listing_name=listing_name)
        #return list_name

    return app
