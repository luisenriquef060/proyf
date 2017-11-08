from django import forms
from .models import ProductoImage
from .models import Vendedor
from .models import Producto

class UploadImageForm(forms.ModelForm):

    class Meta:
        model = ProductoImage
        fields = ['producto', 'image']

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nombre', 'fecha_nacimiento','correo','telefono']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombreP', 'descripcion','precio','compra']
