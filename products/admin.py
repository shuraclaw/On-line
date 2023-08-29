from django.contrib import admin

from .models import *

admin.site.register(Image)
admin.site.register(CatalogItemSubcategory)
admin.site.register(CatalogItemCategory)
admin.site.register(CatalogItem)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Specification)
admin.site.register(Product)
admin.site.register(SaleItem)
admin.site.register(Filter)
