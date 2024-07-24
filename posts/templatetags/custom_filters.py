from django import template
from django.utils.timesince import timesince

register = template.Library()


@register.filter
def timesince_large(date):
    """
    Custom template filter to return the largest time unit for `timesince`.
    """
    time_since = timesince(date)
    time_units = time_since.split(', ')
    if time_units:
        return time_units[0]
    return ''
