from sqlalchemy import create_engine

from tables import Base
from tables.food_entry import FoodEntry
from tables.food import Food
from tables import Session

def main():
    engine = create_engine('postgresql://emily@0.0.0.0/my_metrics')
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    
    session = Session()
    foods = session.query(Food)
    foods_by_name = {}
    for food in foods:
        foods_by_name[food.name] = food
    
    food_entries = session.query(FoodEntry).order_by(FoodEntry.date)
    for entry in food_entries:
        food = foods_by_name[entry.name]
        entry.food = food
    session.commit()

if __name__ == '__main__':
    main()