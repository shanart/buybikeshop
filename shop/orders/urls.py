from django.conf.urls import url
from .views import (
    order_create,
    order_detail,
)

urlpatterns = [
    url(r'^create/$', order_create, name='order_create'),
    url(r'^order/(?P<id>[\w-]+)/$', order_detail, name="detail"),
]
