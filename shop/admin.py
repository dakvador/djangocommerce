from django.contrib import admin

# Register your models here.


from .models import Item, Order, OrderItem


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price','category','photo','description')
    list_display_links = ('title',)
    list_editable = ('price','category','photo','description')
    list_filter = ('title',)
    search_field = ('title',)




@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'item','ordered','quantity')
    list_display_links = ('user',)
    list_editable = ('item','ordered','quantity')
    list_filter = ('user', 'item','ordered')
    search_field = ('user', 'item')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','ordered','ordered_date')
    list_display_links = ('user',)
    list_editable = ('ordered','ordered_date')
    list_filter = ('user', 'ordered')
    search_field = ('user')

