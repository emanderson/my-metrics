import jinja2
import os

class Jinja2Renderer(object):
    def __init__(self, info):
        self.jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates/')))
        
    def __call__(self, value, system):
        template = self.jinja_environment.get_template(system['renderer_info'].name)
        return template.render(value)