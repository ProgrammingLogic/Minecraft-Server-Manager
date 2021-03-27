from flask_sqlalchemy import SQLAlchemy
from workzeug.security import generate_password_hash, check_password_hash
from random import choices

from string import ascii_letters as LETTERS
from string import ascii_digits as DIGITS

class User(db.Model):
    """
    A User of the website.

    Fields:
        id -- The user's unqiue identification string.
        email -- The user's email.
        username -- The user's email.

    Methods:
        set_password -- Set the user's password.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Stirng(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


    def __init__(self, password=None, username=None, email=None, *args, **kwargs):
        """
        Arguments:
            None
        Keyword 11Arguments:
            password -- The user's password.
                Required -- True
                Default Value -- None
            username -- The user's username.
                Required -- True
                Default Value -- None
            email -- The user's email address.
                Required -- True
                Default Value -- None
        """
        super().__init__(*args, **kwargs)


        if password is None:
            raise Exception("Password was not provided.")
        else:
            self.password_hash = generate_password_hash(password)

        if username is None:
            raise Exception("Username was not provided.")
        else:
            self.username = username

        if email is None:
            raise Exception("Email was not provided.")
        else:
            self.email = email

        self.id = create_user_id()


    def create_user_id(self):
        """
        Generates a unique user ID.
        
        Arguments:
            None

        Keyword Arguments:
            None

        Returns:
            None
        """
        new_id = choices(LETTERS + DIGITS, 30)

        while not self.query.filter_by(id=new_id).first() is None:
            new_id = choices(LETTERS + DIGITS, 30)

        return new_id


    def set_password(self, password):
        """
        Sets the user's password.
        
        Arguments:
            password -- The new password.

        Keyword Arguments:
            None

        Returns:
            None
        """
        ps_hash = generate_password_hash(password)


        if ps_hash == self.password:
            raise Exception("Password is the same as previous password.")

        self.password = ps_hash
    

    def check_password(self, password):
        """
        Checks to see if the password matches the user's password.

        Arguments:
            password -- The password to check.

        Keyword Arguments:
            None

        Returns:
            True -- The passwords match.
            False -- The passwords don't match.
        """
        return check_password(self.password_hash, password)


