from django.db import models


class TipoUsuario(models.Model):
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo


class Usuario(models.Model):
    usuario = models.CharField(max_length=15)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    mail = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    telefono = models.IntegerField()
    ciudad = models.CharField(max_length=15)
    direccion = models.CharField(max_length=30)
    sexo = models.CharField(max_length=15)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario


class TipoProducto(models.Model):
    categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.categoria


class Marca(models.Model):
    nombre = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre_producto = models.CharField(max_length=1000)
    stock = models.IntegerField()
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=5000, null=True)
    nuevo = models.BooleanField(null=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True)
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre_producto



