from prisonapp import *


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username=db.Column(db.String(32), unique=True,index=True)
    password_hash=db.Column(db.String(128))
    firstname = db.Column(db.String(30))
    middlename = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    age = db.Column(db.String(5))
    contact = db.Column(db.String(15))
    address = db.Column(db.TEXT())
    birthday = db.Column(db.DATE)
    prisoner = db.Column(db.String(60))
    role_id=db.Column(db.String(2))
    status=db.Column(db.String(20))
    comments = db.relationship('Comment', backref='user', lazy=True)
    visits = db.relationship('Visitation', backref='user', lazy=True)

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer(), primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.TEXT())
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Prisoner(db.Model):
    __tablename__ = 'prisoner'
    id = db.Column(db.Integer(), primary_key=True)
    firstname = db.Column(db.String(30))
    middlename = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    birthday = db.Column(db.DATE)
    age = db.Column(db.String(5))
    crime = db.Column(db.String(60))

class Visitation(db.Model):
    __tablename__ = 'visitation'
    id = db.Column(db.Integer(), primary_key=True)
    vId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    nameP = db.Column(db.String(36), nullable=False)
    date = db.Column(db.DATE, nullable=False)
    numberOfVisitors = db.Column(db.Integer(), nullable=False)
    status = db.Column(db.String(20),nullable=False)

class VisitationLogs(db.Model):
    __tablename__ = 'visitationlogs'
    id = db.Column(db.Integer(), primary_key=True)
    log_vId = db.Column(db.Integer, db.ForeignKey('visitation.id'), nullable=False)
    user_vId = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)


