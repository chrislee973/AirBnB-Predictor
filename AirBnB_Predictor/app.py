from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from .DB_test import DB, Listings
from .updater import add_listing


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)

    @app.route('/')
    def root():
        DB.drop_all()
        DB.create_all()
        return render_template('test.html', title='AirBnB Predictor: Home')
    
    @app.route('/button')
    def button_click():
        return "Hello World! You've clicked me."
    
    @app.route('/new')
    def new_listing():
        return render_template("test.html")

    @app.route('/add', methods=["POST"])
    def add():
        name = request.values["listing_name"]
        city = request.values["city"]
        zipcode = request.values["listing_zipcode"]
        description = request.values["listing_description"]
        amenities = request.values["listing_amenities"]

        #if request.method == "POST":
        add_listing(list_name= name, list_city = city, list_zip=zipcode, list_description = description, list_amenities= amenities)        
        return render_template("test.html", title= "Listing added")
    
    @app.route('/listings', methods=["GET"])
    def listings():
        return render_template("listings.html", title="Listings", listings=Listings.query.all())
    
        
    return app