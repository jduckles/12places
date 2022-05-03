import yaml
from jinja2 import Template

with open('places.yml') as fd:
    places = yaml.load(fd, Loader=yaml.BaseLoader)

with open('places.html') as fd:
    t = Template(fd.read())

filled = t.render(places=places)

print(filled)