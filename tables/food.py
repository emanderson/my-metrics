from sqlalchemy import Column, Integer, String
from tables import Base
from tables.food_to_food_tag import FoodToFoodTag
from sqlalchemy.orm import relationship

class Food(Base):
    __tablename__ = 'food'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    food_tags = relationship("FoodTag", secondary='food_to_food_tag', lazy='joined')
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "<Food('%s')>" % (self.name)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

    
