from django.urls import path

from blog.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path('', Index.as_view(), name='home'),
    path('category/<str:slug>/', PostByCategory.as_view(), name='category'),
    path('post/<str:slug>/', PostView.as_view(), name='post'),
    path('tag/<str:slug>/', PostView.as_view(), name='tag'),
]
