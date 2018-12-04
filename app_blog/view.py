from app_blog.app import app
from flask import render_template

@app.route('/')
def index():
    for i in ('Alex', 'Roma' , 'Tania'):
        name = i
    return render_template('index.html', n=name)

