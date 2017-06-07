from django.contrib import admin

from .models import Product, Wishlist

class WishlistModelAdmin(admin.ModelAdmin):

    list_display = ["user", "item", "created_date"]

    class Meta:
        model = Wishlist

class ProductModelAdmin(admin.ModelAdmin):

    list_display = ["title", "admin_image", "updated", "timestamp", "brand", "category", "year", "subcategory",]
    # list_display_links = ["updated"]

    list_filter = ["brand", "category", "year", "subcategory", "timestamp" ]

    search_fields = ["title", "content"]

    def admin_image(self, obj):
        return '<div><img style="width:100px;height:100px;object-fit:cover" src="%s" /></div>' % obj.cover_image.url

    admin_image.allow_tags = True

    class Meta:
        model = Product

admin.site.register(Product, ProductModelAdmin)
admin.site.register(Wishlist, WishlistModelAdmin)
