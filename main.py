import os
from wsgiref.simple_server import make_server
from pyramid.config import Configurator

if __name__ == '__main__':
    config = Configurator()
    config.add_renderer(name='.html', factory='renderers.jinja2_renderer.Jinja2Renderer')
    
    config.add_route('hello', '/hello/{name}')
    config.add_route('calorie-graph', '/graph')
    
    config.add_static_view('css', 'css')
    
    config.scan('views')
    
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8084, app)
    server.serve_forever()