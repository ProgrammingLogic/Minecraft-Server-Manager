from flask import Flask
from Config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app_config = Config()

app = Flask(__name__)
app.config.from_object(app_config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import User
from app import routes
