from tables.food_entry import FoodEntry
from tables import Base

def upgrade(migrate_engine):
    FoodEntry.__table__.create(migrate_engine)

def downgrade(migrate_engine):
    FoodEntry.__table__.drop(migrate_engine)
