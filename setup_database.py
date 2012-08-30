from sqlalchemy import create_engine

from tables import Base
from tables.food_entry import FoodEntry

def main():
    engine = create_engine('postgresql://emily@0.0.0.0/my_metrics')
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    main()