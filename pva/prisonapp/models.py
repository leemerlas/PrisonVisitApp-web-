from prisonapp import *


class User(db.Model):
    __table__name = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username=db.Column(db.String(32), index=True)
    password_hash=db.Column(db.String(128))
    role_id=db.Column(db.String(2))
    status=db.Column(db.Boolean)

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