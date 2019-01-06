from app_blog.app import app
from flask import render_template
from app_blog.models import Workers

@app.route('/')
def index():

    items = Workers.query.all()

    numb = range(10)
    return render_template('index.html', name=items, numb=numb)


