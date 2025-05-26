from jinja2 import Environment, FileSystemLoader
from datetime import datetime

env = Environment(loader = FileSystemLoader("templates"))
template = env.get_template("helloWorld.jinja")
output = template.render(current_time = datetime.now(), current_date = datetime.now())
print(output)
