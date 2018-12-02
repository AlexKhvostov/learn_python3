from flask import Flask
from app_blog.config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration) # app не получает свойства debug
#print(Configuration.DEBUG)
app.debug = True

#for i in dir(app.debug):
#    print(i)