from flask import Flask, render_template, request, session, redirect, make_response, url_for, flash

from prisonapp import pva


@pva.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print ('b')
        session.pop('user', None)
        session['user'] = request.form['username']
        print session['user']
        print request.form['stat']
        print request.form['roleid']
        if request.form['stat'] == 'PENDING':
            print ('z')
            return redirect('https://pva-web.herokuapp.com/visitor/pending')
        elif request.form['stat'] == 'VERIFIED':
            print ('x')
            if request.form['roleid'] == '2':
                print ('succ')
                return redirect('https://pva-web.herokuapp.com/visitor/landing')
            elif request.form['roleid'] == '1':
                return redirect('https://pva-web.herokuapp.com/clerk/view-announcements')
            elif request.form['roleid'] == '0':
                return redirect('https://pva-web.herokuapp.com/admin/view-announcements')
    return render_template("login-final.html")


@pva.route('/logout')
def logout():
    if session['user'] is None:
        session.pop('user', None)
        return redirect('https://pva-web.herokuapp.com')
    else:
        session.pop('user', None)
        print ('popped!')
        return redirect('https://pva-web.herokuapp.com')


@pva.route('/visitor/landing', methods=['GET'])
def landing_visitor():
    if 'user' in session:
        return render_template("visitor_announcements.html")
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@pva.route('/visitor/schedule', methods=['GET', 'POST'])
def schedule_visit():
    if 'user' in session:
        return render_template('ScheduleOfVisit.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')

@pva.route('/clerk/view_visitors')
def view_visitor():
    if 'user' in session:
        return render_template('visitordata.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@pva.route('/admin/view_visitors')
def view_visitor_admin():
    if 'user' in session:
        return render_template('visitor_data.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@pva.route('/clerk/manage_requests')
def clerk_managerequest():
    if 'user' in session:
        return render_template('visitationreq.html')
    else:
        flash('Error!')
        return render_template('login-final.html')


@pva.route('/admin/visit_logs')
def admin_visitlogs():
    if 'user' in session:
        return render_template('visit_logs.html')
    else:
        flash('Error!')
        return render_template('login-final.html')


@pva.route('/clerk/view_prisoners')
def view_prisoner():
    if 'user' in session:
        return render_template('prisonerdata.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@pva.route('/admin/add_clerk')
def add_clerk():
    if 'user' in session:
        return render_template('add_clerk.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@pva.route('/admin/add_prisoner')
def add_prisoner():
    if 'user' in session:
        return render_template('add_prisoner.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@pva.route('/clerk/record-visitation')
def record_visitation():
    if 'user' in session:
        return render_template('addunregisteredvisitor.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@pva.route('/admin/manage-announcements')
def manage_add():
    if 'user' in session:
        return render_template('create_announcements.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@pva.route('/admin/view-announcements')
def manage_ann():
    if 'user' in session:
        return render_template('manage_announcements.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@pva.route('/admin/view-comments')
def view_com():
    if 'user' in session:
        return render_template('comments.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@pva.route('/admin/manage-prisoner')
def manage_prison():
    if 'user' in session:
        return render_template('prisoner_data.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@pva.route('/clerk/view-announcements')
def manage_ann_clerk():
    if 'user' in session:
        return render_template('ClerkAnnouncements.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@pva.route('/visitor/pending')
def visitor_pending():
    if 'user' in session:
        print('z')
        return render_template('visitorlanding_pending.html')
    else:
        print('x')
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')



@pva.route('/admin/newsupdate')
def newsupdate():
    if 'user' in session:
        return render_template('add-news.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')


@pva.route('/admin/settings')
def adminsetup():
    return render_template('admin_acc.html')


@pva.route('/view_news')
def view_newsupdate():
    return render_template('news.html')

@pva.route('/admin/view-walkin')
def view_walkin():
    if 'user' in session:
        return render_template('getwalkin.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login-final.html')
