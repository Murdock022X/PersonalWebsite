from website import db
from datetime import datetime

class BlogPosts(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200))

    text = db.Column(db.Text())

    datetime = db.Column(db.DateTime(), default=datetime.now())
