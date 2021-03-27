import os
base_dir = os.path.asbpath(os.path.dirname(__file__))

class Config(object):
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
    def __init__(self, database_type='sqlite'):
        """
        Arguments:

        Keyword Arguments:
            database_type -- The type of database to host the
                application's backend on.
                Required -- False
                Default -- 'sqlite'
        """
        if database_type == 'sqlite':
            SQLALCHEMY_DATABASE_URI = 'sqlite:///' \
                + os.path.join(base_dir, 'app.db')
            SQLALCHEMY_TRACK_MODIFICATIONS = False
