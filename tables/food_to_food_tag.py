from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from tables import Base
from tables.food import Food
from tables.food_tag import FoodTag

class FoodToFoodTag(Base):
    __tablename__ = 'food_to_food_tag'
    
    id = Column(Integer, primary_key=True)
    food_id = Column(Integer, ForeignKey('food.id'))
    food_tag_id = Column(Integer, ForeignKey('food_tag.id'))
    
    food = relationship("Food", backref=backref('to_food_tags', order_by=food_id), lazy='joined')
    food_tag = relationship("FoodTag", backref=backref('to_foods', order_by=food_tag_id), lazy='joined')
    
    def __init__(self, food, food_tag):
        self.food = food
        self.food_tag = food_tag
    
    def __repr__(self):
        return "<FoodToFoodTag('%s','%s')>" % (self.food.name, self.food_tag.name)
    
    def to_dict(self):
        return {
            'food': self.food.to_dict(),
            'food_tag': self.food_tag.to_dict()
        }

    
