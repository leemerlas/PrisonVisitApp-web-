from flask import Flask, render_template, request, session, redirect, make_response, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

server = Flask(__name__)



@server.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['login'] == 'Sign in':

                    session.pop('user', None)
                    # pops existing user data, if any!

                    session['user'] = request.form["username"]
                    # if session['role'] == '2':
                    #     return redirect(url_for('landing_visitor'))
                    # elif session['role'] == '1':
                    #     return redirect(url_for('landing_clerk'))
                    # elif session['role'] == '0':
                    #     return redirect(url_for('landing_admin'))

                    print session['user']

    return render_template("login-final.html")

@server.route('/logout')
def logout():
    if session['user'] is None:
        return redirect(url_for('login'))
    else:

        session.pop('user', None)

        return redirect(url_for('login'))



@server.route('/register', methods=['GET','POST'])
def register():
    return render_template("SignUp.html")
  

@server.route('/visitor/landing', methods=['GET'])
def landing_visitor():
    if 'user' in session:
        return render_template("index.html")
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
        return render_template('admin-homepage.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@server.route('/clerk/view_visitors')
def view_visitor():
    if 'user' in session:
        return render_template('view_visitors.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')

@server.route('/clerk/manage_requests')
def clerk_managerequest():
    if 'user' in session:
        return render_template('visitationreq.html')
    else:
        flash('Error!')
        return render_template('login-final.html')


@server.route('/clerk/view_prisoners')
def view_prisoner():
    if 'user' in session:
        return render_template('view_prisoners.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')

@server.route('/admin/visit_logs')
def admin_visitlogs():
    if 'user' in session:
        return render_template('visit_logs.html')
    else:
        flash('Error!')
        return render_template('admin-homepage.html')

@server.route('/admin/add_clerk')
def add_clerk():
    if 'user' in session:
        return render_template('addclerk.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@server.route('/admin/view_visitors')
def view_visitor_admin():
    if 'user' in session:
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