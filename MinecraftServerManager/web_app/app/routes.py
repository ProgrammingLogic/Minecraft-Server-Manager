from flask import render_template


def create_routes(app):
    @app.route('/')
    @app.route('/index.html')
    @app.route('/home')
    def index():
        return render_template("home.html")
