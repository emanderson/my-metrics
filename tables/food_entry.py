from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, backref
from tables import Base
from tables.food import Food

class FoodEntry(Base):
    __tablename__ = 'food_entry'
    
    id = Column(Integer, primary_key=True)
    food_id = Column(Integer, ForeignKey('food.id'))
    calories = Column(Integer)
    date = Column(Date)
    
    food = relationship("Food", backref=backref('food_entries', order_by=date), lazy='joined')
    
    def __init__(self, food, calories, date):
        self.food = food
        self.calories = calories
        self.date = date
    
    def __repr__(self):
        return "<FoodEntry('%s','%s','%s')>" % (self.food.name, self.calories, self.date)
    
    # TODO: name -> food dict
    def to_dict(self):
        return {
            'name': self.food.name,
            'calories': self.calories
        }

    
