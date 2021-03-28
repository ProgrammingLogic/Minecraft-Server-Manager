from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

class FlaskApp():
    def __init__(self):
        self.init_app()
        self.init_db()
        self.init_login_manager()
        self.init_routes()


    def init_app(self):
        """Initialize the app."""
        self.app = Flask(__name__)
        self.app.config.from_object(Config)
        self.db = SQLAlchemy(self.app)
        self.migrate = Migrate(self.app, self.db)


    def init_db(self):
        """
        Initialize the app's database.

        Arguments:
            None

        Keyword Arguments:
            None

        Return Values:
            None
        """
        from models import import_models

        # Store each of the database modules in the app.
        self.app_models = import_models(self)

        for model in self.app_models.items():
            exec(f"""self.{model[0]} = model[1]""")

        self.db.create_all()


    def init_login_manager(self):
        """Initialize the login manager."""
        self.login_manager = LoginManager()
        self.login_manager.init_app(self.app)

        @self.login_manager.user_loader
        def load_user(user_id):
            return self.User.get(user_id)


    def init_routes(self):
        """Initialize the routes."""
        from routes import create_routes
        create_routes(self)


custom_app = FlaskApp()
flask_app = custom_app.app
