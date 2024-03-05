import os
from dotenv import load_dotenv 

load_dotenv()

Download_PATH = 'wkhtmltopdf/bin/wkhtmltopdf.exe'
basedir = os.path.abspath(os.path.dirname(__file__))
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
Download_FOLDER = os.path.join(APP_ROOT, Download_PATH)


class BaseConfig(object):
    """Base configuration."""
    #DADOS DA EMPRESA

    EMPRESA_RSOC = 'Squallo Software'
    EMPRESA_NOMFAN = 'Estatística Municipal'
    EMPRESA_LOGRADOURO = ''
    EMPRESA_NUMLOGR = ''
    EMPRESA_COMPLEMENTO = ''
    EMPRESA_BAIRRO = ''
    EMPRESA_CODMUN = ''
    EMPRESA_CODUF = ''
    EMPRESA_CODPAIS = ''

    #CONFIDENCIAL
#    SECRET_KEY = os.getenv('SECRET_KEY')
#    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')
    SECRET_KEY = 'dev'
    SECURITY_PASSWORD_SALT = 'dev-two'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
#   BANCO DE DADOS
#   SQLITE - LOCALHOST
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLITE_CONNECT = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
    # MYSQL - LOCALHOST
    TYPE_CONNECT = 'mysql'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASS = ''
    MYSQL_PORT = 3308
    MYSQL_DATABASE = 'flask_municipio'
    # MYSQL - LOCALWEB -ANCORAR
    #MYSQL_HOST = 'flask_ancorar.mysql.dbaas.com.br'
    #MYSQL_USER = 'flask_ancorar'
    #MYSQL_PASS = 'Strol!ndi!1'
    #MYSQL_PORT = 3306
    #MYSQL_DATABASE = 'flask_ancorar'
    # MYSQL - DOCKER - LAYOUT
    MYDOCKER_HOST = 'mysql'
    MYDOCKER_USER = 'root'
    MYDOCKER_PASS = 'strolandia'
    MYDOCKER_PORT = 3307
    MYDOCKER_DATABASE = 'docker_flask'
    #CORRESPONDENCIA
    MAIL_SERVER='email-ssl.com.br'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USE_SSL=True
    MAIL_DEFAULT_SENDER="ptarsoneves@squallo.net"
    MAIL_USERNAME='ptarsoneves@squallo.net'
    MAIL_PASSWORD='Pt@rso334@'


    #CORRESPONDENCIA

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
    DEBUG_TB_ENABLED = True


class TestingConfig(BaseConfig):
    """Testing configuration."""
    TESTING = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'
    DEBUG_TB_ENABLED = False
    STRIPE_SECRET_KEY = 'foo'
    STRIPE_PUBLISHABLE_KEY = 'bar'
