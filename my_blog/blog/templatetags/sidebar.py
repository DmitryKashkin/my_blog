from django import template
from blog.models import Post, Tag

register = template.Library()