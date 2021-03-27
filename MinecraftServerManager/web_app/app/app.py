from flask import Flask

from routes import create_routes



app = Flask(__name__)
create_routes(app)


from database import User
