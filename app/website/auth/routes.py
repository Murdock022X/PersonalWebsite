from flask import render_template, Blueprint, redirect, url_for, current_app, flash
from flask_login import current_user, login_required

auth = Blueprint('auth', __name__)
