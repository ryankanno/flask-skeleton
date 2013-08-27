from flask_mail import Mail
from flask.ext.cache import Cache
from flask.ext.seasurf import SeaSurf

mail = Mail()
cache = Cache()
csrf = SeaSurf()
