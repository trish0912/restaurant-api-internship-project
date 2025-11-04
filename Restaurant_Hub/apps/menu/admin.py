
from django.contrib import admin
from .models import MenuItem
from django.utils.html import format_html

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price', 'image_preview')
    search_fields = ('name',)

    # Optional: show image preview in admin list
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50"/>', obj.image.url)
        return "-"
    image_preview.short_description = "Image"
