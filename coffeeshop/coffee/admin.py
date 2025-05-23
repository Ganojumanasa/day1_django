from django.contrib import admin

# Register your models here.
from .models import Coffee





class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity')




admin.site.register(Coffee,CoffeeAdmin)
