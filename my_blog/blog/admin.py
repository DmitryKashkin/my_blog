from django.contrib import admin

from .models import *


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     prepopulated_fields = {'slug': ('title',)}
#
#
# class TagAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     prepopulated_fields = {'slug': ('title',)}
#
#
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)

