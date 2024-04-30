from . import models
from django.shortcuts import render, get_object_or_404


def index_view(request):
    posts = models.Blog.objects.all()
    context = {"posts": posts}
    return render(request, "blog/index.html", context)


def detail_view(request, pk):
    post = get_object_or_404(models.Blog, pk=pk)    
    return render(request, 'blog/detail.html', {'post': post})
