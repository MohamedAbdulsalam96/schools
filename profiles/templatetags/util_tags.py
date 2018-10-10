from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def create_url(url=None, kwargs={}):
    return reverse(url, kwargs=kwargs)
