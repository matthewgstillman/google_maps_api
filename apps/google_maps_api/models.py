from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def login(self, postData):
        return self

    def create_trip(self, postData):
        starting_address = postData['starting_address']
        ending_address = postData['ending_address']
        return self

class Trip(models.Model):
    starting_address = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
# Create your models here.
