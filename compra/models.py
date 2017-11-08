from django.db import models
from django.contrib import admin

# Create your models here.
class Vendedor(models.Model):

    nombre =   models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    correo = models.CharField(max_length=40)
    telefono = models.IntegerField()

    def __str__(self):

        return self.nombre

class Producto(models.Model):
    nombreP    = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=160)
    precio = models.IntegerField()
    compra   = models.ManyToManyField(Vendedor)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def __str__(self):
        return self.nombreP

class ProductoImage(models.Model):
    producto = models.ForeignKey(Producto, related_name='images')
    image = models.ImageField(upload_to='compra/images/')

    def __unicode__(self,):
        return str(self.image)
