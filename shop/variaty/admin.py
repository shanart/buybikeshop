from django.contrib import admin
from .models import Category, Subcategory, Brand

class SubcategoryModelAdmin(admin.ModelAdmin):

    list_display = ["title", "parent"]
    # list_display_links = ["updated"]

    list_filter = ["parent"]

    search_fields = ["title", "content"]

    class Meta:
        model = Subcategory

admin.site.register(Category)
admin.site.register(Subcategory, SubcategoryModelAdmin)
admin.site.register(Brand)
