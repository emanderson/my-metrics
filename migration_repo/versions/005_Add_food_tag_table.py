from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FoodTag(Base):
    __tablename__ = 'food_tag'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

def upgrade(migrate_engine):
    FoodTag.__table__.create(migrate_engine)

def downgrade(migrate_engine):
    FoodTag.__table__.drop(migrate_engine)
