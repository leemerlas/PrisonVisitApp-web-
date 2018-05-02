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



@server.route('/register', methods=['GET','POST'])
def register():
    return render_template("SignUp.html")
  

@server.route('/visitor/landing', methods=['GET'])
def landing_visitor():
    if 'user' in session and session['role'] == '2':
        return render_template("landing_visitor.html")
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')



@server.route('/visitor/schedule', methods=['GET','POST'])
def schedule_visit():
    if 'user' in session:
        return render_template('schedule_visitor.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')

@server.route('/visitor/comments')
def post_comment():
    if 'user' in session:
        return render_template('comment_visitor.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@server.route('/clerk/landing')
def landing_clerk():
    if 'user' in session:
        return render_template('landing_clerk.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')

@server.route('/admin/landing')
def landing_admin():
    if 'user' in session:
        return render_template('landing_admin.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@server.route('/clerk/view_visitors')
def view_visitor():
    if 'user' in session and session['role'] == '1':
        return render_template('view_visitors.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')

@server.route('/clerk/manage_requests')
def clerk_managerequest():
    if 'user' in session and session['role'] == '1':
        return render_template('visitrequest_clerk.html')
    else:
        flash('Error!')
        return render_template('login-final.html')


@server.route('/clerk/view_prisoners')
def view_prisoner():
    if 'user' in session and session['role'] == '1':
        return render_template('view_prisoners.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@server.route('/admin/add_clerk')
def add_clerk():
    if 'user' in session and session['role'] == '0':
        return render_template('addclerk.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@server.route('/admin/view_visitors')
def view_visitor_admin():
    if 'user' in session and session['role'] == '0':
        return render_template('view_visitors_admin.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')

CORS(server)
server.config['CORS_HEADERS'] = 'Content-Type'
server.config['SECRET_KEY'] = 'thisissecret'

server.secret_key = os.urandom(24)

if __name__=='__main__':
    server.run(host='localhost', port=8000, debug=True)
