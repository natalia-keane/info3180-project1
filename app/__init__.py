from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://hyioekpiaplpxj:b42b34dee0e7d13a5e3ad113ab6300d472683a9b2bafa8f68cb9109587badbf7@ec2-50-19-109-120.compute-1.amazonaws.com:5432/d8go17643lcfna"# "postgresql://project1:password@localhost/project1" #
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
