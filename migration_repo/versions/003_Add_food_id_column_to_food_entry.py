from sqlalchemy import Table, MetaData, Integer, ForeignKey, Column

def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    food = Table('food', meta, autoload=True)
    food_entry = Table('food_entry', meta, autoload=True)
    food_id = Column('food_id', Integer, ForeignKey('food.id'))
    food_id.create(food_entry)

def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    food_entry = Table('food_entry', meta, autoload=True)
    food_entry.c.food_id.drop()
