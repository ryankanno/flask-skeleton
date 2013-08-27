from flask_mail import Mail
from flask.ext.cache import Cache
from flask.ext.seasurf import SeaSurf
from flask.ext.bcrypt import Bcrypt

cache = Cache()
csrf = SeaSurf()
mail = Mail()
bcrypt = Bcrypt()
