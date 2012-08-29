from pyramid.view import view_config

@view_config(route_name='hello', renderer='test.html')
def hello_world(request):
    return {'hello': request.matchdict['name']}