from sqlalchemy import MetaData, Table, Column, Integer, ForeignKey

meta = MetaData()

food_to_food_tag = Table(
    'food_to_food_tag', meta,
    Column('id', Integer, primary_key=True),
    Column('food_id', Integer, ForeignKey('food.id')),
    Column('food_tag_id', Integer, ForeignKey('food_tag.id'))
)

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    food = Table('food', meta, autoload=True)
    food_tag = Table('food_tag', meta, autoload=True)
    food_to_food_tag.create()

def downgrade(migrate_engine):
    meta.bind = migrate_engine
    food_to_food_tag.drop()
