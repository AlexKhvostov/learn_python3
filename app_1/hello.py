from flask import Flask, url_for, request, render_template
app = Flask(__name__)
app.debug = True

@app.route('/',methods=['GET', 'POST'])
def index():
    return 'Index Page'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


















'''-----------------------------------------------------------------'''
'''-----------------------------------------------------------------'''
'''-----------------------------------------------------------------'''
'''-----------------------------------------------------------------'''

@app.route('/user/<username>')
def show_user_profile(username):
    # показать профиль данного пользователя
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # вывести сообщение с данным id, id - целое число
    return 'Post %d' % post_id
'''
int	принимаются целочисленные значения
float	как и int, только значения с плавающей точкой
path	подобно поведению по умолчанию, но допускаются слэши
'''
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


if __name__ == '__main__':
    app.run()