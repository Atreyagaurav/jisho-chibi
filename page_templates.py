
from jinja2 import Template
from window import resource


csspath = resource("./templates/style.css")


def get_intro_html():
    with open(resource("./templates/intro.htm"), "r") as r:
        template = Template(r.read())
    return template.render(csspath=csspath)


def get_meanings_html(word):
    with open(resource("./templates/definition.htm"), "r") as r:
        template = Template(r.read())
    return template.render(word=word, csspath=csspath)
    
