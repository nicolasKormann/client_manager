from flask import Flask, Blueprint, redirect, render_template, Response
from flask_login import login_required


pages = Blueprint('pages', __name__)


@pages.route('/login', methods=['GET'])
def index():
    return render_template('login.html')

@pages.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@pages.route('/customers', methods=['GET'])
@login_required
def profile():
    return render_template('customers.html')

@pages.route('/contacts', methods=['GET'])
@login_required
def contacts():
    return render_template('contacts.html')
