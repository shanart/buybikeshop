from django import template
from django.db.models import Count # to count something :)
from django.utils.safestring import mark_safe
# import markdown

register = template.Library()

from variaty.models import Subcategory, Brand, Category

@register.inclusion_tag('widgets/categories_list.html')
def show_category_list():
    categories = Category.objects.all()
    return {'categories': categories}

@register.inclusion_tag('widgets/brand_list.html')
def show_brand_list():
    brands = Brand.objects.all()
    return {'brands': brands}
