from app_blog.app import app
from app_blog.app import db
import app_blog.view

from app_blog.posts.blueprint import posts

app.register_blueprint(posts, url_prefix='/blog')

if __name__ == '__main__':
    app.run()