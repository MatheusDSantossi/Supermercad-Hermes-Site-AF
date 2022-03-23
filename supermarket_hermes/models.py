from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ("-added",)

    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("supermarket_hermes:detail", kwargs={"slug": self.slug})
    