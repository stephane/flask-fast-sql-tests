from sqlalchemy import func

from .database import db


class Hive(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)


class Bee(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    birthdate = db.Column(db.DateTime(timezone=True), default=func.now())
    hive_id = db.Column(db.Integer, db.ForeignKey('hive.id'))
    hive = db.relationship(Hive, backref=db.backref('hive'))

    def __repr__(self):
        return "%s %s" % (self.kind, self.name)

