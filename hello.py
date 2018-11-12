from flask import Flask
app = Flask(__name__)



@app.route('/')
def index():
    return 'index file'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<username>')
def show_user_profile(username):
    # показать профиль данного пользователя
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # выводит сообщение с данным id/ id - целое число
    return 'Post %d' % post_id


if __name__=='__main__':
    app.run(debug=True)
