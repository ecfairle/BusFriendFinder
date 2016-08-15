import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
CLIENT_ID = "82e7ed9be8f841838c7103c980911daa"
CLIENT_SECRET = "82e7ed9be8f841838c7103c980911daa"

WTF_CSRF_ENABLED = True
SECRET_KEY = 'akeyortwo'
