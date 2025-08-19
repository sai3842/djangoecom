from django.contrib import admin
from .models import Product
from men_shoes.models import product_db

admin.site.register(Product)
admin.site.register(product_db)


# Register your models here.



