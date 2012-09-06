from sqlalchemy import Table, MetaData, Integer, ForeignKey, Column, String

def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    food_entry = Table('food_entry', meta, autoload=True)
    food_entry.c.name.drop()

def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    food = Table('food', meta, autoload=True)
    food_entry = Table('food_entry', meta, autoload=True)
    name = Column('name', String)
    name.create(food_entry)
