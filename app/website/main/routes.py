from flask import render_template, Blueprint, redirect, url_for, current_app, flash
from flask_login import current_user, login_required
from website import models

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    """
    Flask route that returns webpage for info on the project.

    :return: Rendered index.html webpage.
    """

    return render_template('index.html')