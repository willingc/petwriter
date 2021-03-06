from django.db import models
from django.contrib import admin
import django.contrib.auth.models


class Pet(models.Model):
    # Every Pet has a user. This means that a user can own between 0 and infinity pets.
    user = models.ForeignKey(django.contrib.auth.models.User)

    # Every pet has a (unique across all pets) name. For convenience,
    # we use the Django SlugField.
    name = models.SlugField(unique=True)

    # Add a field for pet description. We set the default to be the empty string,
    # and we set blank=True to lazy people people to have empty descriptions.
    description = models.CharField(max_length=1024, default='', blank=True)

class Update(models.Model):
    pub_date = models.DateTimeField(
        # Use current time on obj creation.
        auto_now_add=True,
    )
    pet = models.ForeignKey(Pet)
    text = models.CharField(max_length=140)

admin.site.register(Update)
admin.site.register(Pet)
