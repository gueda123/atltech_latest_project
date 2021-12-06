# Generated by Django 3.2.5 on 2021-12-06 10:46

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('discription', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='post_img')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='post_img')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='post_img')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='post_img')),
                ('img5', models.ImageField(blank=True, null=True, upload_to='post_img')),
                ('img6', models.ImageField(blank=True, null=True, upload_to='post_img')),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 6, 16, 46, 41, 205517))),
            ],
        ),
        migrations.CreateModel(
            name='Blogs_Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_subject', models.CharField(max_length=255)),
                ('comment_text', models.TextField()),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 6, 16, 46, 41, 206518))),
                ('Blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.blog_post')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
