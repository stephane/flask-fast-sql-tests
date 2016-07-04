from flask.ext.sqlalchemy import SQLAlchemy

# no app object passed! Instead we use use db.init_app in the factory.
db = SQLAlchemy()