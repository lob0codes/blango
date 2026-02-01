from django.contrib.auth.models import User
from django.utils.html import format_html
from django import template

register = template.Library()

@register.filter
def author_details(author: User):
  if not author:
    return ''

  first_name = author.first_name
  last_name = author.last_name

  if first_name and last_name:
    name = f'{first_name} {last_name}'

  else:
    name = author.username
  
  email = author.email

  if email:
    return format_html('<a href="mailto:{}">{}</a>', email, name)
 
  return name

