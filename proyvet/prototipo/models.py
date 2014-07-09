from django.db import models
from datetime import datetime

# Create your models here.

LUGARES_CHOISES = (
    ('depto', 'Departamento'),
    ('casa', 'Casa'),
    ('campo', 'Campo'),
    ('Silo_de_soja', 'Silo de Soja'),
)

class Cliente(models.Model):
    nombre = models.CharField(max_length=75)
    apellido = models.CharField(max_length=75)
    domicilio = models.CharField(max_length=75)
    telefono = models.IntegerField() # change for format phone
    email = models.EmailField(max_length=254)


class Especie(models.Model):
    nombre = models.CharField(max_length=75, unique=False)
    descripcion = models.CharField(max_length=75)


class Raza(models.Model):
    especie = models.ForeignKey(Especie, verbose_name="Especie del animal", related_name="raza")
    nombre = models.CharField(max_length=75)


class Paciente(models.Model):
    nombre = models.CharField(max_length=75)
    edad = models.IntegerField(blank=True)
    raza = models.ForeignKey(Raza, verbose_name="raza del animal", related_name="paciente")
    sexo = models.CharField(max_length=75, blank=True)
    convNinos = models.BooleanField(default=False)
    convAnimales = models.BooleanField(default=False)
    lugar = models.CharField(max_length=64, choices=LUGARES_CHOISES, blank=True)
    castrado = models.BooleanField()
    #enfermedades <-
    peso = models.FloatField(blank=True)
    foto = models.ImageField(blank=True, upload_to="fotos")
    reproductor = models.BooleanField(blank=True)
    collar = models.CharField(max_length=75, blank=True)
    #alergias
    #pelaje va a ser una clase
    #cirugia
    chip = models.BooleanField(blank=True)


class DescripcionServicio(models.Model):
    descripcion = models.CharField(max_length=75)
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=True)


class DescripcionServicioVacunacion(DescripcionServicio):
    vacuna = models.ForeignKey(TipoVacuna, verbose_name="referencia a la vacuna", related_name="descripcionServicioVacunacion")


class Servicios(models.Model):
    paciente = models.ForeignKey(Paciente, verbose_name="animal tratado", related_name="servicios")
    descripcion = models.ForeignKey(DescripcionServicio, verbose_name="Tratamiento", related_name="servicios")
    costoCongelado = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fechaInicio = models.DateField(default=datetime.today())
    fechaFin = models.DateField(default=datetime.today())


class Pagos(models.Model):
    servicios = models.ForeignKey(Paciente, verbose_name="pagos del tratamiento", related_name="pagos")
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateField(blank=True)
    # cobrador TODO

"""
#class Vacuna(models.Model):
    dosis etc... TODO
"""

class TipoVacuna(models.Model): #tipo de vacuna por ahora
    paciente = models.ManyToManyField(Paciente, related_name="vacuna")

