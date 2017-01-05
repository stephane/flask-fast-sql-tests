from flask import url_for

from beehive.database import db
from beehive import models as beehive_models
from beehive import factories as beehive_factories

def test_hive_instance(session):
    hive = beehive_models.Hive(name='H1')
    db.session.add(hive)
    db.session.commit()
    assert beehive_models.Hive.query.count() == 1
    assert hive.name == 'H1'

def test_hive_factory(session):
    hive = beehive_factories.HiveFactory()
    db.session.add(hive)
    assert beehive_models.Hive.query.count() == 1

def test_hive_list(session, client):
    hive1 = beehive_models.Hive(name='H1')
    hive2 = beehive_models.Hive(name='H2')
    session.add_all([hive1, hive2])
    session.commit()

    assert beehive_models.Hive.query.count() == 2
    response = client.get(url_for('beehive.hive_list'))
    data = response.get_data(as_text=True)
    assert hive1.name in data
    assert hive2.name in data
