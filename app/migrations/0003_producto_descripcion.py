# Generated by Django 4.1.2 on 2022-11-26 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_marca_producto_nuevo_producto_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
