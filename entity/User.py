from exts import db


class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_name=db.Column(db.String(10),nullable=False,default='xxx')
    user_passwd=db.Column(db.String(15),nullable=False,default='123456')
    user_phone=db.Column(db.String(13),nullable=False,default='155AAAABBBB')


