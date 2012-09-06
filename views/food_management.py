from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from tables.food import Food
from tables.food_tag import FoodTag
from tables import Session

@view_config(route_name='food-list', renderer='food_list.html')
def food_list(request):
    session = Session()
    foods = session.query(Food).order_by(Food.name)
    session.close()
    return {'title': 'Foods', 'foods': foods}

@view_config(route_name='food-tag-list', renderer='food_tag_list.html')
def food_tag_list(request):
    session = Session()
    food_tags = session.query(FoodTag).order_by(FoodTag.name)
    session.close()
    return {'title': 'Food Tags', 'food_tags': food_tags}

@view_config(route_name='food-tag-add-form', renderer='food_tag_add_form.html')
def food_tag_add_form(request):
    return {'title': 'Add a Food Tag'}

@view_config(route_name='food-tag-add')
def food_tag_add(request):
    name = request.params['name']
    
    session = Session()
    new_tag = FoodTag(name)
    session.add(new_tag)
    session.commit()
    
    return HTTPFound('/food_tag/list')
