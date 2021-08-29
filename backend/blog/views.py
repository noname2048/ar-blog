from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from blog.models import Post


# class PostLV(ListView):
#     model = Post
#     template_name = "blog/post_list.html"


# class PostDV(DetailView):
#     model = Post


class PostListTV(TemplateView):
    template_name = "blog/post_list.html"


class PostDetailTV(TemplateView):
    template_name = "blog/post_detail.html"
