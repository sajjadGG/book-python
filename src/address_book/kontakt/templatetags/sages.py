from django import template

register = template.Library()

@register.filter
def podmien_literki(ciag_znakow):
    return ciag_znakow.replace('a', 'xxx')