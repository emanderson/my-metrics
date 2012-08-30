from datetime import date
from datetime import timedelta

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from tables.food_entry import FoodEntry
from tables import Session

@view_config(route_name='calorie-graph', renderer='calorie_graph.html')
def calorie_graph(request):
    return {'title': 'Calorie Graph'}

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