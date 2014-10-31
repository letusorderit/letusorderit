from django.contrib import admin
from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('master', 'description', 'shop_url', 'get_item_count')
    search_fields = ('master', 'description')

    def get_item_count(self, obj):
        return obj.orderitem_set.count()
    get_item_count.short_description = 'Item count'


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('get_order_description', 'user_email', 'item_identifier',
                    'count')
    search_fields = ('user_email', 'item_identifier')

    def get_order_description(self, obj):
        return obj.order.description


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
