import pytest

from beehive import create_app
from beehive.database import db as _db

@pytest.fixture(scope='session')
def app(request):
    """Session-wide test `Flask` application."""
    app = create_app('config.TestingConfig')

    ctx = app.app_context()
    ctx.push()

    def tearDown():
        ctx.pop()

    request.addfinalizer(tearDown)
    return app

@pytest.yield_fixture(scope='session')
def client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='session')
def db(app, request):
    """Session-wide test database."""
    _db.init_app(app)
    _db.create_all()

    def teardown():
        _db.drop_all()

    request.addfinalizer(teardown)
    return _db

@pytest.fixture(scope='function')
def session(db, request):
    """Creates a new database session for a test."""
    db.session.begin_nested()

    def teardown():
        db.session.rollback()
        db.session.close()

    request.addfinalizer(teardown)
    return db.session

