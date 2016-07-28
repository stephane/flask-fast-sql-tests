import click

from flask import Flask

def create_app(config_object):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)
    # register_cli is only called when necessary

    return app


def register_extensions(app):
    from .database import db
    db.init_app(app)


def register_blueprints(app):
    from beehive.hives.views import hives
    app.register_blueprint(hives, url_prefix='/hives')


def register_cli(app):
    @app.cli.command(short_help="Initialize the database")
    def initdb():
        click.echo("Create tables of %s" % app.config['SQLALCHEMY_DATABASE_URI'])
        from .database import db
        db.create_all()