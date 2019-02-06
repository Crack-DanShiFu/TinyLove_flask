from exts import db


class BannerInfo(db.Model):
    __tablename__ = 'bannerinfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(10), nullable=True, default='xxx')
    url = db.Column(db.String(100), nullable=True, default='http://127.0.0.1:5000/static/defult.png')
