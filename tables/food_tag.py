from sqlalchemy import Column, Integer, String
from tables import Base

class FoodTag(Base):
    __tablename__ = 'food_tag'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "<FoodTag('%s')>" % (self.name)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }