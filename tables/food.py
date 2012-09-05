from sqlalchemy import Column, Integer, String, Date
from tables import Base

class Food(Base):
    __tablename__ = 'food'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "<Food('%s')>" % (self.name)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

    
