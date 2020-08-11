from django.template import Library

register = Library()

@register.filter()
def to_float(value):
    return float(value)
