from django.db import models
import datetime
from django.utils.text import slugify
from django.db.models import fields
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth.models import User

from datetime import datetime

class Category(models.Model):
    title 		= models.CharField(max_length=120)
    slug 		= models.SlugField(blank=True)
    user 		= models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    characteristics = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

class Brand(models.Model):
    title 		= models.CharField(max_length=120)
    slug 		= models.SlugField(blank=True)
    user 		= models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    country 	= models.CharField(max_length=120, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Brand, self).save(*args, **kwargs)

class Subcategory(models.Model):
    title 		= models.CharField(max_length=120)
    slug 		= models.SlugField(blank=True)
    parent 		= models.ForeignKey(Category, default=1)
    # manufacturer = models.ForeignKey(Brand, default=1)
    user 		= models.ForeignKey(settings.AUTH_USER_MODEL, default=1)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Subcategory, self).save(*args, **kwargs)
