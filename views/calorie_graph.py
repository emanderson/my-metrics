from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

@view_config(route_name='calorie-graph', renderer='calorie_graph.html')
def calorie_graph(request):
    return {'title': 'Calorie Graph'}

@view_config(route_name='food-entry-add-form', renderer='food_entry_add.html')
def food_entry_add_form(request):
    return {'title': 'Add a Food Entry'}

@view_config(route_name='food-entry-add')
def food_entry_add(request):
    return HTTPFound('/food_entry/add_form')