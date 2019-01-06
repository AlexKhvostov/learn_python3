from flask import Flask
from app_blog.config import Configuration

from flask_sqlalchemy import SQLAlchemy





app = Flask(__name__)
app.config.from_object(Configuration) # app не получает свойства debug


db = SQLAlchemy(app)

