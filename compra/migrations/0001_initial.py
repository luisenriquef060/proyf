# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 21:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreP', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=160)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductoImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='compra/images/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='compra.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
                ('correo', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='compra',
            field=models.ManyToManyField(to='compra.Vendedor'),
        ),
    ]