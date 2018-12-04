from flask import Flask
from app_blog.config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration) # app не получает свойства debug
app.debug = True
