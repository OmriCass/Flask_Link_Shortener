from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import string
import random

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///./testdb.db'

    db.init_app(app)

    #imports later on

    migrate = Migrate(app, db)

    return app