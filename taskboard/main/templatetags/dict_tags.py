"""файл с тегом keyvalue для шаблона """
from django import template

register = template.Library()

@register.filter(name="keyvalue")
def keyvalue(dictionary, key):
    """шаблонный тег. Возвращает значение по ключу. Если нет ключа, возвращает пустую строку"""
    try:
        return dictionary[key]
    except KeyError:
        return ''
