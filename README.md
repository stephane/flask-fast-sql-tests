Fast SQL tests for Flask
========================

This project provides support for running unit tests using the database
without  recreating the database between each test. Test isolation is
provided by the scoped sessions of SQLAlchemy. The interesting bits
are in ``tests/conftest.py``.

If you are interested, the git history contains another approach based
savepoints in commit e1dbca7.

Install
-------

    $ pip install -r requirements_dev.txt -e .

The application requires a database called ``beehive`` (you can change it in
``config.py``).

Run
---

The app (but only tests are interesting in this project...):

    $ export FLASK_APP=app
    $ flask initdb
    $ flask run


The tests:

    $ python setup.py test

or

    $ py.test -s
