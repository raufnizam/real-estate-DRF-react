from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField


class Tag(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("index", args=(str(self.id)))

AVAILABILITY_CHOICES = (
    ('yes','YES'),
    ('no', 'NO'),
    
)


class Property(models.Model):
    title = models.CharField(max_length=200)
    snippet = models.CharField(max_length=200)
    title_tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="properties")
    # header_img = models.ImageField(upload_to="images/", null=True, blank=True)
    # wide_angle_img = models.ImageField(upload_to="images/", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    availability = models.CharField(max_length=6, choices=AVAILABILITY_CHOICES, default='yes')
    address = models.CharField(max_length=200)
    country = CountryField(blank_label='(Select country)', blank=True, null=True)
    price = models.CharField(max_length=200)
    # description = RichTextField(blank=True, null=True)
    description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="some_property")
    
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("property_detail", kwargs={"pk": self.pk})


    
class Comments(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.property.title} - {self.author.username}"