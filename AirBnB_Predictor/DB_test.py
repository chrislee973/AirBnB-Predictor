from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Listings(DB.Model):
    #id= DB.Column(DB.BigInteger, primary_key = True) # id column (primary key)
    name = DB.Column(DB.String, nullable=False)
    city = DB.Column(DB.String, nullable = False)
    zipcode = DB.Column(DB.BigInteger, primary_key=True)
    description = DB.Column(DB.String)
    amenities = DB.Column(DB.String)

