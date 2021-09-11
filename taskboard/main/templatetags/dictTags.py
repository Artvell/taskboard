from django import template

register = template.Library()

@register.filter(name="keyvalue")
def keyvalue(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return ''