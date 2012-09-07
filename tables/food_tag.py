from sqlalchemy import Column, Integer, String
from tables import Base
from tables.food_to_food_tag import FoodToFoodTag
from sqlalchemy.orm import relationship

class FoodTag(Base):
    __tablename__ = 'food_tag'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    foods = relationship("Food", secondary='food_to_food_tag')
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "<FoodTag('%s')>" % (self.name)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }