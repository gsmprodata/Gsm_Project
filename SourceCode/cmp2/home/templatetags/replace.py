from django import template

register = template.Library()

@register.filter
def rep(value):
    return value.replace(" ","")
def ini(list,i):
    return list[i]
@register.filter
def strip(str):
    return str.strip()
