from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Category, Tag


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload', 'author', 'category', 'tag']


class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_count'] = Post.objects.filter(category=None).count()
        return context


class PostDetail(DetailView):
    model = Post


def single_post_page(request, post_num):
    post = Post.objects.get(pk=post_num)

    return render(request, 'blog/post_detail.html', {'post': post, })


def categories_page(request, slug):
    if slug == 'no-category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    context = {
        'categories': Category.objects.all(),
        'category': category,
        'post_list': post_list,
        'no_category_count': Post.objects.filter(category=None).count(),
    }
    return render(request, 'blog/post_list.html', context)


def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    context = {
        'tag': tag,
        'categories': Category.objects.all(),
        'post_list': post_list,
        'no_category_count': Post.objects.filter(category=None).count(),
    }
    return render(request, 'blog/post_list.html', context)