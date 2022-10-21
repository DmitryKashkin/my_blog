from django.urls import path

from blog.views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('category/<str:slug>', Category.as_view(), name='category'),
]
