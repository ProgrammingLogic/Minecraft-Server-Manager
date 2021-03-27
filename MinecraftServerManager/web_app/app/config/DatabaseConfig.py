import os
base_dir = os.path.abspath(os.path.dirname(__file__))

class DatabaseConfig(object):
    """
    Configuration for the web app.

    Fields:
        SQLALCHEMY_DATABASE_URI -- The URI for the SQL database.
        SQLALCHEMY_TRACK_MODIFICATIONS - Whether or not to track SQL
          modifications.

    Methods:
        None

    TODO: Move away from SQLite and towards PostGreSQL.
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' \
        + os.path.join(base_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
