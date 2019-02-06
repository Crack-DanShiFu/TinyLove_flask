from flask import Flask, render_template
import config
from entity.BannerInfo import BannerInfo
from entity.User import User
from exts import db
import json

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user_info')
def query_user():
    users = User.query.all()
    info = {}
    for user in users:
        info[user.id] = [user.user_name, user.user_passwd, user.user_phone]
    print(info)
    result = json.dumps(info)
    return result


@app.route('/get_banner_info')
def get_banner_info():
    banners = BannerInfo.query.all()
    info = {}
    for banner in banners:
        info[banner.id] = [banner.title, banner.url]
    print(info)
    result = json.dumps(info)
    return result


if __name__ == '__main__':
    app.run()
