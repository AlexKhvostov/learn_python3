from app_blog.app import app
from flask import render_template


@app.route('/')
def index():
    user1 = ('1', 'Alex', 'admin',      '21.01.1997', '500')
    user2 = ('2', 'Roma', 'admin',      '22.07.1985', '500')
    user3 = ('3', 'Vova', 'Tester',     '01.06.1988', '400')
    user4 = ('4', 'sasha', 'developer', '06.08.1997', '800')
    user5 = ('5', 'ivan', 'users',      '08.09.1992', '700')


    items =[user1, user2, user3, user4, user5]
    numb = range(10)
    return render_template('index.html', name=items, numb=numb)


