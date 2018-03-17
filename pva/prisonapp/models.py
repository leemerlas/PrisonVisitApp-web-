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
    address = db.Column(db.Text(255))
    birthday = db.Column(db.DATE)
    prisoner = db.Column(db.String(60))
    role_id=db.Column(db.String(2))
    status=db.Column(db.Boolean)
    comments = db.relationship('Comment', backref='user', lazy=True)
    related_to = db.relationship('Prisoner', backref='user', lazy=True)

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer(), primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text(256))
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Prisoner(db.Model):
    __tablename__ = 'prisoner'
    id = db.Column(db.Integer(), primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    firstname = db.Column(db.String(30))
    middlename = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    birthday = db.Column(db.DATE)
    age = db.Column(db.String(5))

# class RevokedTokenModel(db.Model):
#     __tablename__ = 'revoked_tokens'
#     id = db.Column(db.Integer, primary_key=True)
#     jti = db.Column(db.String(120))
#
#     def add(self):
#         db.session.add(self)
#         db.session.commit()
#
#     @classmethod
#     def is_jti_blacklisted(cls, jti):
#         query = cls.query.filter_by(jti=jti).first()