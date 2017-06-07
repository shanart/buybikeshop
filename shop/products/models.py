from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from datetime import datetime
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User

from comments.models import Comment
from variaty.models import Category, Brand, Subcategory

def upload_location(instance, filename):
    return "products/%s/%s" %(instance.id, filename)

# Create your models here.
class Product(models.Model):
    title           = models.CharField(max_length=120)
    user            = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        limit_choices_to={'groups__name': "Manager"},
                        default=1)
    brand           = models.ForeignKey(Brand, default=1)
    category        = models.ForeignKey(Category, blank=True, null=True)
    subcategory		= models.ForeignKey(Subcategory, blank=True, null=True)
    description     = models.TextField(default=False)
    content         = models.TextField(default=False)
    year            = models.IntegerField(blank=True, null=True)

    cover_image     = models.ImageField(
                        upload_to=upload_location,
                        null=True,
                        blank=True)

    slug            = models.SlugField(unique=True, blank=True, null=True)
    price 			= models.FloatField()
    draft           = models.BooleanField(default=False)
    publish     	= models.DateTimeField(default=datetime.now())
    updated         = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp       = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    class Meta:
        ordering = ('-publish', )

    # TODO:
    #  - make @property for order stuf


class Wishlist(models.Model):
    item = models.ForeignKey(Product)
    user = models.ForeignKey(User)
    created_date = models.DateTimeField(default=datetime.now())
    """
        TODO : add quantity

    """
    def __str__(self):
        return self.user.username

