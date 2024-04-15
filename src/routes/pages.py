from flask import Flask, Blueprint, redirect, render_template, Response


pages = Blueprint('pages', __name__)


@pages.route('/login', methods=['GET'])
def index():
    return render_template('login.html')

@pages.route('/dash', methods=['GET'])
def dash():
    return render_template('dash.html')
