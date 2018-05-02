from flask import Flask, render_template, request, session, redirect, make_response, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from prisonapp.models import User
from werkzeug.security import check_password_hash
from flask_cors import CORS
import os

server = Flask(__name__)


@server.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['login'] == 'Sign in':

            user = User.query.filter_by(username=request.form['username']).first()

            if user is None:
                flash('Username or password invalid!')
                return redirect(url_for('login'))
            else:
                if check_password_hash(user.password_hash, request.form['password']):
                    session.pop('user', None)
                    session.pop('fname', None)
                    session.pop('public_id', None)
                    session.pop('role', None)
                    # pops existing user data, if any!

                    session['user'] = user.username
                    session['fname'] = user.firstname
                    session['public_id'] = user.public_id
                    session['role'] = user.role_id

                    print session['user']

                    # if session['role'] == '2':
                    #     return redirect(url_for('landing_visitor'))
                    # elif session['role'] == '1':
                    #     return redirect(url_for('landing_clerk'))
                    # elif session['role'] == '0':
                    #     return redirect(url_for('landing_admin'))

    return render_template("login-final.html")


@server.route('/logout')
def logout():
    if session['user'] is None:
        return redirect(url_for('login'))
    else:

        session.pop('user', None)
        session.pop('fname', None)
        session.pop('public_id', None)
        session.pop('role', None)

        return redirect(url_for('login'))


@server.route('/visitor/landing', methods=['GET'])
def landing_visitor():
    if 'user' in session:
        if session['role'] == '2':
            return render_template("index.html")
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@server.route('/clerk/landing')
def landing_clerk():
    if 'user' in session:
        if session['role'] == '1':
            return render_template('landing_clerk.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@server.route('/admin/manage-announcements')
def manage_announcements():
    if 'user' in session:
        return render_template('manage_announcements.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


CORS(server)
server.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:1234@localhost/prisonapp'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dc = SQLAlchemy(server)
server.config['USE_SESSION_FOR_NEXT'] = True
server.config['CORS_HEADERS'] = 'Content-Type'
server.config['SECRET_KEY'] = 'thisissecret'

server.secret_key = os.urandom(24)

if __name__ == '__main__':
    server.run(host='localhost', port=8080, debug=True)
