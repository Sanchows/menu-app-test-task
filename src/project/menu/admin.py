from django.contrib import admin

from menu.models import Item, Menu


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    exclude = ('level',)


admin.site.register(Menu)
