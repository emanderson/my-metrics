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
    food_entries = session.query(FoodEntry).order_by(FoodEntry.date)
    for entry in food_entries:
        food_name = entry.name
        existing_food = session.query(Food).filter_by(name=food_name).all()
        if len(existing_food) == 0:
            new_food = Food(food_name)
            session.add(new_food)
    session.commit()

if __name__ == '__main__':
    main()