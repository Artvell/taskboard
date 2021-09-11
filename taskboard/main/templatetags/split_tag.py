"""файл с шаблонным тегом split"""
from django import template
register = template.Library()

@register.filter(name='split')
def split(value, arg):
    """шаблонный тег, разбивает строку по разделителю arg"""
    return value.split(arg)
