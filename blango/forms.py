from django import forms
from blog.models import Comment

class CommentForm(ModelForm):
  class Me