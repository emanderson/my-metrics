from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='hello', renderer='test.html')
def hello_world(request):
    return {'hello': 'world'}

if __name__ == '__main__':
    config = Configurator()
    config.add_renderer(name='.html', factory='renderers.jinja2_renderer.Jinja2Renderer')
    config.add_route('hello', '/hello/{name}')
    #config.add_view(hello_world, route_name='hello', renderer='test.html')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8084, app)
    server.serve_forever()