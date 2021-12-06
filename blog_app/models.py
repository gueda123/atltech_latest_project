from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from django.db import models
from app_1.models import User
from datetime import datetime



class blog_post(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    discription = RichTextField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True, upload_to='post_img')
    time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title

    def qty_comments(self):
        return Blogs_Comments.objects.filter(Blog_id=self.id).count()


class Blogs_Comments(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Blog = models.ForeignKey(blog_post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.User.email + " - "+ self.Blog.title
