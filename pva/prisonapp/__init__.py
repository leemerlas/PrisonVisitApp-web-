from flask import Flask, Blueprint, request, abort,url_for, jsonify, g, render_template, make_response,session
from flask_sqlalchemy import SQLAlchemy
import os, sqlalchemy, jwt, datetime
from flask_httpauth import HTTPBasicAuth
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask_cors import CORS
from datetime import date


pva = Flask(__name__)

cors = CORS(pva)

pva.config['USE_SESSION_FOR_NEXT'] = True
pva.config['CORS_HEADERS'] = 'Content-Type'
pva.config['SECRET_KEY'] = 'thisissecret'
pva.secret_key = os.urandom(24)

from prisonapp import server

