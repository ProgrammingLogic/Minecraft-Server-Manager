from flask import render_template


def Home_create(app, db):
    @app.route('/')
    @app.route('/index.html')
    @app.route('/home')
    def index():
        return render_template("home.html")
