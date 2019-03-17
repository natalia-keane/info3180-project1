from . import db
from werkzeug.security import generate_password_hash


class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(255))
    upload = db.Column(db.String(150))
    profile_creation =db.Column(db.String(255))
    
    def __init__(self, fname, lname, username, password):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)




    
        