from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET-KEY'] = 'kdskdjasdlsj kkdjoem,c pqwe2341'

    return app

