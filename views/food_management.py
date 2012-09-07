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

@view_config(route_name='food-edit-food-tags-form', renderer='food_edit_food_tags_form.html')
def food_edit_food_tags_form(request):
    session = Session()
    food = session.query(Food).filter_by(id=request.matchdict['id']).first()
    food_tags = session.query(FoodTag).order_by(FoodTag.name).all()
    session.close()
    return {'title': 'Edit Tags for %s' % food.name, 'food': food, 'tags': food_tags}

@view_config(route_name='food-edit-food-tags')
def food_edit_food_tags(request):
    food_id = request.matchdict['id']
    tag_ids = map(int, request.params.getall('tag_id'))
    session = Session()
    food = session.query(Food).filter_by(id=food_id).first()
    already_tagged = []
    to_remove = []
    for food_tag in food.food_tags:
        if not food_tag.id in tag_ids:
            to_remove.append(food_tag)
        else:
            already_tagged.append(food_tag.id)
    for tag in to_remove:
        food.food_tags.remove(tag)
    to_add = session.query(FoodTag).filter(FoodTag.id.in_(set(tag_ids)-set(already_tagged))).all()
    food.food_tags.extend(to_add)
    session.commit()
    
    return HTTPFound('/food/list')
