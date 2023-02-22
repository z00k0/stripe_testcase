from django.contrib import admin
from stripetest.models import Item, OrderDetail, Order


class ItemAdmin(admin.ModelAdmin):
    pass


class OrderDetailAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Order, OrderAdmin)
