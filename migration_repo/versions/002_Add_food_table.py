from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Food(Base):
    __tablename__ = 'food'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

def upgrade(migrate_engine):
    Food.__table__.create(migrate_engine)

def downgrade(migrate_engine):
    Food.__table__.drop(migrate_engine)
