import factory

from . import models as beehive_models

class CustomSQLAlchemyModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        return model_class(*args, **kwargs)

class HiveFactory(CustomSQLAlchemyModelFactory):
    class Meta:
        model = beehive_models.Hive

    name = factory.Sequence(lambda n: "H%d" % n)
