from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template('test.html', title='Home')
    
    @app.route('/button')
    def button_click():
        return "Hello World! You've clicked me."
    
    # @app.route('/new')
    # def new_listing():
    #     return render_template("base.html")

    # @app.route('/add', methods=["POST"])
    # @app.route('/listings', methods=["GET"])
    # def add_listing():
    #     if request.method == "POST":
    #         add_listing()
        
    #     return render_template("listings.html", listings=Listings.query.all())
    
    
        
    return app