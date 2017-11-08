from django.contrib import admin
from .models import Vendedor
from .models import ProductoImage
from .models import Producto
# Register your models here.
admin.site.register(Vendedor)
admin.site.register(Producto)
admin.site.register(ProductoImage)
