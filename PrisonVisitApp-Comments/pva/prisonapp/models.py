from prisonapp import *


class Comments(db.Model):
    __table__name = 'comments'
    cid = db.Column(db.Integer(), primary_key=True)
    vid = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(60), nullable=False)
    date = db.Column(db.DATE(), nullable=False)