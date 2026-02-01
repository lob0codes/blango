from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from blog.models import Post

def index(req):
  posts = Post.objects.filter(published_at__lte=timezone.now())
  print(len(posts))
  return render(req, 'blog/index.html', {'posts': posts})

def post_detail(req, slug):
  post = get_object_or_404(Post, slug=slug)

  return render(req, 'blog/post-detail.html', {'post': post})