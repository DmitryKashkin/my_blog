from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView

from blog.models import *


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context


# class Index(View):
#
#     def get(self, request, *args, **kwargs):
#         return render(request, 'blog/index.html')


class Category(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'blog/category.html')


class Post(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'blog/index.html')
