from tables.food import Food
from tables import Base

def upgrade(migrate_engine):
    Food.__table__.create(migrate_engine)

def downgrade(migrate_engine):
    Food.__table__.drop(migrate_engine)
