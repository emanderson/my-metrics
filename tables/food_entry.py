from sqlalchemy import Column, Integer, String, Date
from tables import Base

class FoodEntry(Base):
    __tablename__ = 'food_entry'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    calories = Column(Integer)
    date = Column(Date)
    
    def __init__(self, name, calories, date):
        self.name = name
        self.calories = calories
        self.date = date
    
    def __repr__(self):
        return "<FoodEntry('%s','%s','%s')>" % (self.name, self.calories, self.date)
    
    def to_dict(self):
        return {
            'name': self.name,
            'calories': self.calories
        }

    
