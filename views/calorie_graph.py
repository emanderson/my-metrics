import csv

from datetime import date
from datetime import timedelta

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from tables.food import Food
from tables.food_entry import FoodEntry
from tables.food_tag import FoodTag
from tables import Session
from utils.lose_it_data_reader import LoseItDataReader
from utils.food_day import FoodDay

@view_config(route_name='calorie-graph', renderer='calorie_graph.html')
def calorie_graph(request):
    session = Session()
    food_entries = session.query(FoodEntry).order_by(FoodEntry.date)
    food_days = FoodDay.group_days(food_entries)
    session.close()
    return {'title': 'Calorie Graph', 'food_entries': food_entries, 'food_days': food_days}
    
@view_config(route_name='calorie-graph-data', renderer='json')
def calorie_graph_data(request):
    session = Session()
    food_entries = session.query(FoodEntry).order_by(FoodEntry.date).all()
    food_days = FoodDay.group_days(food_entries)
    tags = session.query(FoodTag).order_by(FoodTag.id)
    session.close()
    return {'food_days': map(lambda x: x.to_dict(), food_days), 'tags': map(lambda x: x.to_dict(), tags)}

@view_config(route_name='food-entry-add-form', renderer='food_entry_add.html')
def food_entry_add_form(request):
    return {'title': 'Add a Food Entry'}

@view_config(route_name='food-entry-add')
def food_entry_add(request):
    name = request.params['name']
    calories = int(request.params['calories'])
    day = date.today() - timedelta(int(request.params['days_ago']))
    
    session = Session()
    existing_food = session.query(Food).filter_by(name=food_name).all()
    food = None
    if len(existing_food) == 0:
        food = Food(food_name)
        session.add(food)
    else:
        food = existing_food[0]
    new_entry = FoodEntry(food, calories, day)
    session.add(new_entry)
    session.commit()
    
    return HTTPFound('/food_entry/add_form')

@view_config(route_name='food-entry-list', renderer='food_entry_list.html')
def food_entry_list(request):
    session = Session()
    food_entries = session.query(FoodEntry).order_by(FoodEntry.date)
    food_days = FoodDay.group_days(food_entries)
    session.close()
    return {'title': 'Food Entries', 'food_entries': food_entries, 'food_days': food_days}

@view_config(route_name='lose-it-upload-form', renderer='lose_it_upload.html')
def lose_it_upload_form(request):
    return {'title': 'Upload LoseIt Data'}

@view_config(route_name='lose-it-upload', renderer='ignored_food_entries.html')
def lose_it_upload(request):
    session = Session()
    
    # TODO: duplicate detection
    input_file = request.POST['file'].file
    reader = LoseItDataReader(input_file)
    existing_for_date = {}
    ignored = []
    for entry in reader:
        existing_food = session.query(Food).filter_by(name=entry.name).all()
        food = None
        if len(existing_food) == 0:
            food = Food(entry.name)
            session.add(food)
        else:
            food = existing_food[0]
        if not entry.date in existing_for_date:
            existing_entries = session.query(FoodEntry).filter_by(date=entry.date).all()
            existing_for_date[entry.date] = existing_entries
        if existing_for_date[entry.date]:
            ignored.append(entry)   
        else:
            new_entry = FoodEntry(food, entry.calories, entry.date)
            session.add(new_entry)
    
    session.commit()
    if ignored:
        return {'title': 'Existing Data Not Imported', 'ignored': ignored}
    else:
        return HTTPFound('/food_entry/lose_it_upload_form')