from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post


def single_post_page(request, post_num):
    post = Post.objects.get(pk=post_num)

    return render(request, 'blog/post_detail.html', {'post': post, })
