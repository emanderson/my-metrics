from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FoodEntry(Base):
    __tablename__ = 'food_entry'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    calories = Column(Integer)
    date = Column(Date)

def upgrade(migrate_engine):
    FoodEntry.__table__.create(migrate_engine)

def downgrade(migrate_engine):
    FoodEntry.__table__.drop(migrate_engine)
