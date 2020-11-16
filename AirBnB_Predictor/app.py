from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template('test.html', title='Home')
    
    @app.route('/button')
    def button_click():
        return "Hello World! You've clicked me."
        
    return app