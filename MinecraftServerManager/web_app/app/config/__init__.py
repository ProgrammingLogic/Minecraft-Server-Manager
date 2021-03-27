from .DatabaseConfig import DatabaseConfig

class Config(object):
    """
    The global flask configuration object.

    This configuration object combines all the Flask configuration
    objects into one, allowing to run configure just once, and
    allowing for segemented parts of the application for better code
    design and organization.

    Fields:

    Methods:

    """
    SQLALCHEMY_DATABASE_URI = DatabaseConfig.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = DatabaseConfig.SQLALCHEMY_TRACK_MODIFICATIONS
