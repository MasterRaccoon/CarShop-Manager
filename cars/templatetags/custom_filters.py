from django import template

register = template.Library()

@register.filter(name='split_first')
def split_first(value):
	if isinstance(value, str):
		return value.split(' ')[0]
	return value
