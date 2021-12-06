from django.contrib import admin
from .models import blog_post, Blogs_Comments
# Register your models here.

admin.site.register(blog_post)
admin.site.register(Blogs_Comments)