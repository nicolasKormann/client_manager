from flask import Flask, Blueprint, redirect, render_template, Response
from flask_login import login_required


pages = Blueprint('pages', __name__)


@pages.route('/login', methods=['GET'])
def index():
    return render_template('login.html')

@pages.route('/dash', methods=['GET'])
def dash():
    return render_template('dash.html')

@pages.route('/customers', methods=['GET'])
@login_required
def profile():
    return render_template('customers.html')
