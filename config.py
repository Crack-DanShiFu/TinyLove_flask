DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '47.107.173.225'
PORT = '3306'
DATABASE = 'tinylove'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(
    DIALECT,
    DRIVER,
    USERNAME,
    PASSWORD,
    HOST,
    PORT,
    DATABASE
)

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@47.107.173.225:3306/springMVC'
# 'mysql+pymysql://用户名称:密码@localhost:端口/数据库名称'
SQLALCHEMY_TRACK_MODIFICATIONS = True
