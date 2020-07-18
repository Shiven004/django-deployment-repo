from django import template


#Creating templates Library object
register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string.
    """
    return value.replace(arg, '')

#register
#register.filter('cut',cut)
