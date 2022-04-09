from django.contrib import admin
from .models import Accessories
# Register your models here.
class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')
admin.site.register(Accessories, AccessoriesAdmin)
