from django.contrib.auth.models import User
from django.utils.html import format_html
from django import template
from blog.models import Post

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

@register.simple_tag
def row(extra_classes=''):
  return format_html('<div class="row {}">', extra_classes)

@register.simple_tag
def col(extra_classes=''):
  return format_html('<div class= "col {}">', extra_classes)

@register.simple_tag
def enddiv():
  return format_html('</div>')

@register.inclusion_tag('blog/post-list.html')
def recent_posts(post):
  posts = Post.objects.exclude(pk=post.pk)[:5]
  return {
    'title': 'Recent Posts', 'posts': posts
  }