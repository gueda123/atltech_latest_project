from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('blog_details/<int:pk>', views.blog_details, name="blog_details"),
    path('post_comment', views.post_comment, name="post_comment"),
]