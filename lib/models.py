from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    author_name = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, null=False, blank=False)
    published_year = models.CharField(max_length=255, null=True, blank=True)
    pages = models.CharField(max_length=255, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255, null=False, blank=False)
    updated_date = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name