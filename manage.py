from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from exts import db
from entity.User import User
from entity.BannerInfo import BannerInfo

from app import app

manage = Manager(app)
migrate = Migrate(app, db)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
