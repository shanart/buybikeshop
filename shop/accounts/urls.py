from django.conf.urls import url
from django.contrib import admin


from .views import (
    login_view,
    register_view,
    logout_view,
    user_panel,
    update,
)


urlpatterns = [

    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^dashboard/', user_panel, name='user_panel'),
    url(r'^update/', update, name='update'),

    # url(r'^dashboard/', user_panel, name='dashboard'),
    # url(r'^user/', user_panel, name='dashboard'),
    # url(r'^avatar/', include('avatar.urls')),

    # url(r'^$', product_list, name='list'),
    # url(r'^product/(?P<slug>[\w-]+)/$', product_detail, name="detail"),
    # url(r'^category/(?P<slug>[\w-]+)/$', product_filter_by_category, name="product_filter_by_category"),
    # url(r'^brand/(?P<slug>[\w-]+)/$', product_filter_by_brand, name="product_filter_by_brand"),
    # url(r'^create/$', category_create),
    # url(r'^(?P<slug>[\w-]+)/edit/$', category_update, name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', category_delete),
]
