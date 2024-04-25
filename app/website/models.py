from flask_login import UserMixin

from website import db, login_manager

# Users table and loader to facilitate login for flask site.
@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True)

    password_hash = db.Column(db.String(100))

class BlogPosts(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200))

    text = db.Column(db.Text())
