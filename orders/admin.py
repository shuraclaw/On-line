from django.contrib import admin

from .models import *

admin.site.register(OrderProduct)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Basket)
admin.site.register(BasketProduct)
