from flask import url_for

from beehive.database import db
from beehive.hives import models as hives_models
from beehive.hives import factories as hives_factories

def test_hive_instance(session):
    hive = hives_models.Hive(name='H1')
    db.session.add(hive)
    db.session.commit()
    assert hives_models.Hive.query.count() == 1
    assert hive.name == 'H1'

def test_hive_factory(session):
    hive = hives_factories.HiveFactory()
    db.session.add(hive)
    assert hives_models.Hive.query.count() == 1

def test_hive_list(session, client):
    hive1 = hives_models.Hive(name='H1')
    hive2 = hives_models.Hive(name='H2')
    session.add_all([hive1, hive2])
    session.commit()

    assert hives_models.Hive.query.count() == 2
    response = client.get(url_for('hives.hive_list'))
    data = response.get_data(as_text=True)
    assert hive1.name in data
    assert hive2.name in data
