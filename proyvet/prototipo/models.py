from django.db import models
from datetime import datetime

# Create your models here. NO quiero xD

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

    #constructor de clase
   

class Especie(models.Model):
    nombre = models.CharField(max_length=75, unique=False)
    descripcion = models.CharField(max_length=75)

    #constructor de clase
    def __init__(self, nombre,descripcion):
        
        if(nombre and descripcion):
                self.nombre = nombre
                self.descripcion = descripcion
                
        else:
            raise InfoEspecieIncorrecta("Faltan datos para crear Especie")


class Raza(models.Model):

    especie = models.ForeignKey(Especie, verbose_name="Especie del animal", related_name="raza")
    nombre = models.CharField(max_length=75)

    #constructor de clase. Se necesita el id de especie para crear.

    def __init__(self, nombre_especie,nombre):

        if(nombre_especie):
            aux = Objects.Especie.get(nombre=nombre_especie)
            if(aux):
                if(nombre):
                    self.especie = aux
                    self.nombre = nombre
                else:
                    raise InfoRazaIncorrecta("Debe ingresar el nombre de la raza")
            else:
                raise RazaEspecieIncorrecta("La especie no existe")
        else:
            raise RazaInfoEspecieVacia("El campo nombre_especie es obligatorio")

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

    #constructor de clase. Se necesita el id de la raza

    def __init__(self, nombre, edad, id_raza, sexo, convNinos="", convAnimales="", lugar="", 
        castrado="", peso="", foto="", reproductor="", collar="", chip=""):

        if(raza):
            aux = Objects.Raza.get(nombre = id_raza)
            if(aux):
                if(nombre and edad and sexo):
                    self.nombre = nombre
                    self.edad = edad
                    self.raza = aux
                    self.sexo = sexo
                else:
                    raise PacienteInfoIncorrecta("Los campos nombre, edad y sexo son obligatorios")
            else:
                raise RazaEspecieIncorrecta("La raza no existe")
        else:
            raise RazaInfoEspecieVacia("El campo raza es obligatorio")

        self.convNinos = convNinos
        self.convAnimales = convAnimales
        self.lugar = lugar
        self.castrado = castrado
        self.peso = peso
        self.reproductor = reproductor
        self.collar = collar
        self.chip = chip

class DescripcionServicio(models.Model):
    descripcion = models.CharField(max_length=75)
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __init__(self, descripcion, costo):

        if(descripcion and costo):
            self.descripcion = descripcionServicioVacunacion
            self.costo = costo
        else:
            raise DescripcionServicioInfoIncorrecta("Los campos descripcion y costo son obligatorios")

class Servicios(models.Model):
    paciente = models.ForeignKey(Paciente, verbose_name="animal tratado", related_name="servicios")
    descripcion = models.ForeignKey(DescripcionServicio, verbose_name="Tratamiento", related_name="servicios")
    costoCongelado = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fechaInicio = models.DateField(default=datetime.today())
    fechaFin = models.DateField(default=datetime.today())

    #constructor de clase. Se necesitan los id de descripcion y paciente.
    def __init__(self, id_paciente, id_descripcion, costoCongelado="", fechaInicio="", fechaFin=""):

        if(id_paciente and id_descripcion):
            aux_paciente = Objects.Paciente.get(id = id_paciente)
            aux_descripcion = Objects.DescripcionServicio.get(id = id_descripcion)
            if(aux_paciente and aux_descripcion):
                self.paciente = aux_paciente
                self.descripcion = aux_descripcion
                self.costoCongelado = aux_descripcion.costo
            else:
                raise ServiciosInfoIncorrecta("Los campos paciente o descripcion son incorrectos")
        else:
            raise ServiciosInfoVacia("Los campos paciente o descripcion son obligatorios")

        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin



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

class DescripcionServicioVacunacion(DescripcionServicio):
    vacuna = models.ForeignKey(TipoVacuna, verbose_name="referencia a la vacuna", related_name="descripcionServicioVacunacion")