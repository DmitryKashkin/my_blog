from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView


class Index(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'blog/index.html')


class Category(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'blog/category.html')
