from django.db import models
from app_1.models import User
from app_1.models import Products
from datetime import datetime
from django.core.validators import FileExtensionValidator



    
    
class home_benner(models.Model):
    class Meta:
        verbose_name_plural = 'Home Banner'
        
    title = models.CharField(max_length=255, null=True, blank=True)
    header = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    benner = models.ImageField(upload_to='Home_benner/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'webp'])], help_text = "Choose Only .jpg, .jpeg, .png, .webp files PLease..")
    button_link = models.URLField(null=True, blank=True)


class home_little_benner(models.Model):
    class Meta:
        verbose_name_plural = 'Home Little Banner'
    title = models.CharField(max_length=255, null=True, blank=True, default="1")
    benner = models.ImageField(upload_to='home_little_benner/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'webp'])], help_text = "Choose Only .jpg, .jpeg, .png, .webp files PLease..")
    button_link = models.URLField(null=True, blank=True, default='')


class home_bottom_benner(models.Model):
    class Meta:
        verbose_name_plural = 'Home Bottom Banner'
    title1 = models.CharField(max_length=255, null=True, blank=True)
    title2 = models.CharField(max_length=255, null=True, blank=True)
    up_text = models.CharField(max_length=255, null=True, blank=True)
    home_bottom_benner = models.ImageField(upload_to='home_bottom_benner/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'webp'])], help_text = "Choose Only .jpg, .jpeg, .png, .webp files PLease..")
    button_link = models.URLField(null=True, blank=True, default='')
        
      
class home_side_benner(models.Model):
    class Meta:
        verbose_name_plural = 'Home side Banner'
    title = models.CharField(max_length=255, null=True, blank=True)
    home_side_benner = models.ImageField(upload_to='home_bottom_benner/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'webp'])], help_text = "Choose Only .jpg, .jpeg, .png, .webp files PLease..")
    button_link = models.URLField(null=True, blank=True, default='')
        
        
class Shop_now_page_benner(models.Model):
    class Meta:
        verbose_name_plural = 'Shop Now Page Banner'
    title = models.CharField(max_length=255, null=True, blank=True)
    title2 = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    Shop_now_page_benner = models.ImageField(upload_to='Shop_now_page_benner/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'webp'])], help_text = "Choose Only .jpg, .jpeg, .png, .webp files PLease..")
        
    
        
        
