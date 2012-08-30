from pyramid.view import view_config

@view_config(route_name='calorie-graph', renderer='calorie_graph.html')
def calorie_graph(request):
    return {'title': 'Calorie Graph'}