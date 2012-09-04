import os
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from sqlalchemy import create_engine
from tables import Session

if __name__ == '__main__':
    engine = create_engine('postgresql://emily@0.0.0.0/my_metrics')
    Session.configure(bind=engine)

    config = Configurator()
    config.add_renderer(name='.html', factory='renderers.jinja2_renderer.Jinja2Renderer')
    
    config.add_route('hello', '/hello/{name}')
    config.add_route('calorie-graph', '/graph')
    config.add_route('calorie-graph-data', '/graph/data')
    config.add_route('food-entry-add-form', '/food_entry/add_form')
    config.add_route('food-entry-add', '/food_entry/add', request_method='POST')
    config.add_route('food-entry-list', '/food_entry/list')
    config.add_route('lose-it-upload-form', '/food_entry/lose_it_upload_form')
    config.add_route('lose-it-upload', '/food_entry/lose_it_upload', request_method='POST')
    
    config.add_route('dynamic-css', '/css/{name}.css')
    
    # TODO: do dynamic file merging for JS like CSS
    config.add_static_view('js', 'js')
    
    config.scan('views')
    
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8084, app)
    server.serve_forever()