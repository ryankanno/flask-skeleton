from flask_mail import Mail
from flask.ext.cache import Cache
from flask.ext.seasurf import SeaSurf
from flask.ext.bcrypt import Bcrypt
from flask.ext.restful import Api

mail = Mail()
cache = Cache()
csrf = SeaSurf()
bcrypt = Bcrypt()
api = Api()
