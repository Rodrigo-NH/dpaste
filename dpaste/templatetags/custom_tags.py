from django import template
from dpaste.apps import dpasteAppConfig

register = template.Library()

# remember giving acccess to any dpasteAppConfig is not secure
ALLOWABLE_VALUES = ("HEADLINE_TEXT",)

@register.simple_tag
def settings_value(name):
    if name in ALLOWABLE_VALUES:        
        return getattr(dpasteAppConfig, name, '')
    return ''
    