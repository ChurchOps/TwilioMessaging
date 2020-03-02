import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_dropzone import Dropzone
from dotenv import load_dotenv

load_dotenv(verbose=True)

app = Flask(__name__)

app.secret_key = os.getenv('SECRET')
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
dropzone = Dropzone(app)

from app import routes, models
