from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(request, 'blog/index.html', {'posts': posts, })


def single_post_page(request, post_num):
    post = Post.objects.get(pk=post_num)

    return render(request, 'blog/single_post_page.html', {'post': post, })
