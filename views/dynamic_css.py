from datetime import date
from datetime import timedelta
import os

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from pyramid.response import Response

# TODO: minify, versioning, etc.
@view_config(route_name='dynamic-css')
def calorie_graph(request):
    name = request.matchdict['name']
    files_to_join = []
    if name == 'main':
        files_to_join = [
            'reset.css',
            'main.css'
        ]
    elif name == 'graph':
        files_to_join = [
            'graph.css'
        ]
    else:
        return HTTPNotFound('File %s.css does not exist' % name)
    content = ''
    for filename in files_to_join:
        f = file('css/' + filename, 'r')
        content += f.read() + '\n'
        f.close()
    return Response(content, content_type='text/css')