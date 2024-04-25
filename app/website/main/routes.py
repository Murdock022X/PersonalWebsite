from flask import render_template, Blueprint, redirect, url_for, current_app, flash, current_app
from flask_login import current_user, login_required
from website.models import BlogPosts
from pathlib import Path
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    """
    Flask route that returns webpage for info on the project.

    :return: Rendered index.html webpage.
    """

    return render_template('index.html')

@main.route('/blog/<int:page>')
def blog(page=1):
    """
    Flask route that returns webpage for info on the project.

    :return: Rendered index.html webpage.
    """

    pagination = BlogPosts.query.order_by(BlogPosts.datetime.desc()).paginate(page=page)

    return render_template('blog.html', pagination=pagination)

@main.route('/documents')
def documents():
    """
    Flask route that returns webpage for info on the project.

    :return: Rendered index.html webpage.
    """

    filesFolder = current_app.config['ROOT'] / Path('static/files')

    files = []

    for path in filesFolder.iterdir():
        fileTime = datetime.fromtimestamp(path.lstat().st_mtime)
        files.append((path.name, fileTime.strftime('%Y-%m-%d %H:%M:%S')))

    return render_template('documents.html', files=files)
