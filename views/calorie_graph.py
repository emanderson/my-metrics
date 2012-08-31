import csv

from datetime import date
from datetime import timedelta

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from tables.food_entry import FoodEntry
from tables import Session
from utils.lose_it_data_reader import LoseItDataReader
from utils.food_day import FoodDay

@view_config(route_name='calorie-graph', renderer='calorie_graph.html')
def calorie_graph(request):
    session = Session()
    food_entries = session.query(FoodEntry).order_by(FoodEntry.date)
    food_days = FoodDay.group_days(food_entries)
    return {'title': 'Calorie Graph', 'food_entries': food_entries, 'food_days': food_days}
    
@view_config(route_name='calorie-graph-data', renderer='json')
def calorie_graph_data(request):
    session = Session()
    food_entries = session.query(FoodEntry).order_by(FoodEntry.date)
    food_days = FoodDay.group_days(food_entries)
    return {'food_days': map(lambda x: x.to_dict(), food_days)}

@view_config(route_name='food-entry-add-form', renderer='food_entry_add.html')
def food_entry_add_form(request):
    return {'title': 'Add a Food Entry'}

@view_config(route_name='food-entry-add')
def food_entry_add(request):
    name = request.params['name']
    calories = int(request.params['calories'])
    day = date.today() - timedelta(int(request.params['days_ago']))
    
    new_entry = FoodEntry(name, calories, day)
    session = Session()
    session.add(new_entry)
    session.commit()
    
    return HTTPFound('/food_entry/add_form')

@view_config(route_name='lose-it-upload-form', renderer='lose_it_upload.html')
def lose_it_upload_form(request):
    return {'title': 'Upload LoseIt Data'}

@view_config(route_name='lose-it-upload')
def lose_it_upload(request):
    session = Session()
    
    input_file = request.POST['file'].file
    reader = LoseItDataReader(input_file)
    for entry in reader:
        new_entry = FoodEntry(entry.name, entry.calories, entry.date)
        session.add(new_entry)
    
    session.commit()
    return HTTPFound('/food_entry/lose_it_upload_form')