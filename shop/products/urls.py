from django.conf.urls import url
from django.contrib import admin

from .views import (
    product_list,
    product_filter_by_category,
    product_filter_by_brand,
    product_detail,
    add_to_wishlist,
    remove_from_wishlist,
)

urlpatterns = [
    url(r'^$', product_list, name='list'),
    url(r'^product/(?P<slug>[\w-]+)/$', product_detail, name="detail"),
    url(r'^category/(?P<slug>[\w-]+)/$', product_filter_by_category, name="product_filter_by_category"),
    url(r'^brand/(?P<slug>[\w-]+)/$', product_filter_by_brand, name="product_filter_by_brand"),
    url(r'^wishlist-add/(?P<id>[\w-]+)/$', add_to_wishlist, name="add_to_wishlist"),
    url(r'^wishlist-remove/(?P<id>[\w-]+)/$', remove_from_wishlist, name="remove_from_wishlist"),
    # url(r'^create/$', category_create),
    # url(r'^(?P<slug>[\w-]+)/edit/$', category_update, name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', category_delete),
]
