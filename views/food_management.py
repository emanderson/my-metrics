from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from tables.food import Food
from tables import Session

@view_config(route_name='food-list', renderer='food_list.html')
def food_entry_list(request):
    session = Session()
    foods = session.query(Food).order_by(Food.name)
    session.close()
    return {'title': 'Foods', 'foods': foods}

