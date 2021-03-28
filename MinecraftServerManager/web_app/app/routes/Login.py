from flask import render_template
from flask_login import current_user, login_user


def Login_create(FlaskApp):
    app = FlaskApp.app
    db = FlaskApp.db
    User = FlaskApp.User

    @app.route('/login', methods=['GET', 'POST'])
    @app.route('/signin', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('home'))

        return render_template('login.html')
