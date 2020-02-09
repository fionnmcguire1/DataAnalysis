# app.config["DEBUG"] = True
# app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///dataanalysis.db'
# #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'dataanalysis.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)
