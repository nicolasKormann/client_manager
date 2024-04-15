from flask import Flask, Blueprint, redirect, render_template, Response, request, url_for
from dataclasses import dataclass
from flask_login import login_user
import requests
from oauthlib.oauth2 import WebApplicationClient
from oauthlib.oauth2.rfc6749.errors import InvalidGrantError
from dotenv import load_dotenv
import os
from src.controllers.login_manager import User

load_dotenv()


auth_routes = Blueprint('auth_routes', __name__)


GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')


oauth = WebApplicationClient(client_id=GOOGLE_CLIENT_ID)


@dataclass
class GoogleHosts:
    authorization_endpoint: str
    token_endpoint: str
    userinfo_endpoint: str
    certs: str


def get_google_oauth_url():
    hosts = requests.get('https://accounts.google.com/.well-known/openid-configuration')
    if hosts.status_code != 200:
        raise Exception('Error getting google hosts')
    
    data = hosts.json()
    
    return GoogleHosts(authorization_endpoint=data.get('authorization_endpoint'), token_endpoint=data.get('token_endpoint'), userinfo_endpoint=data.get('userinfo_endpoint'), certs=data.get('jwks_uri'))

@auth_routes.route('/auth/login', methods=['GET'])
def login():
    hosts = get_google_oauth_url()

    redirect_uri = oauth.prepare_request_uri(
        uri=hosts.authorization_endpoint,
        redirect_uri='https://localhost:5000/auth/callback',
        scope=['openid', 'email', 'profile']
    )

    return redirect(location=redirect_uri)


@auth_routes.route('/auth/callback', methods=['GET'])
def callback():
    code = request.args.get('code')
    hosts = get_google_oauth_url()
    try:
        token_url, headers, body = oauth.prepare_token_request(
            token_url=hosts.token_endpoint,
            authorization_response=request.url,
            redirect_url='https://localhost:5000/auth/callback',
            code=code,
            client_secret=GOOGLE_CLIENT_SECRET
        )

        token_response = requests.post(token_url, headers=headers, data=body)
        oauth.parse_request_body_response(token_response.text)
        uri, headers, body = oauth.add_token(hosts.userinfo_endpoint)
        userinfo_response = requests.get(uri, headers=headers, data=body)
    except InvalidGrantError:
        return redirect(url_for('auth_routes.login'))

    userinfo_response = requests.get(uri, headers=headers, data=body)
    user = User(userinfo_response.json()['sub'])
    login_user(user)
    return render_template('dash.html', userinfo=userinfo_response.json())

