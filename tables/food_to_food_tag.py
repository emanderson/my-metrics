from sqlalchemy import Column, Integer, ForeignKey
from tables import Base

class FoodToFoodTag(Base):
    __tablename__ = 'food_to_food_tag'
    
    id = Column(Integer, primary_key=True)
    food_id = Column(Integer, ForeignKey('food.id'))
    food_tag_id = Column(Integer, ForeignKey('food_tag.id'))
    
