from django.contrib import admin

# Register your models here.
from .models import Tables,Product

admin.site.register(Tables)
admin.site.register(Product)