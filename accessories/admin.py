from django.contrib import admin
from .models import Accessorie, Order
from django.utils.html import format_html
# Register your models here.
class AccessoriesAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.accessories_photo.url))
    thumbnail.short_description = 'Accessories Image'
    list_display = ('id' , 'thumbnail' , 'title', 'price', 'category')
    list_display_links = ('id', 'thumbnail', 'title')
admin.site.register(Accessorie, AccessoriesAdmin)
admin.site.register(Order)
