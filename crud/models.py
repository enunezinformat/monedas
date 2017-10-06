from django.db import models

# Create your models here.
class Monedas(models.Model):
    nombre = models.CharField(max_length=30,blank=False,unique=False)
    abreviacion = models.CharField(max_length=3,blank=False,unique=False)

    def __str__(self):
        return self.nombre

class Paridades(models.Model):
    moneda  = models.ForeignKey(Monedas)
    fecha   = models.DateField()
    paridad = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return str(self.moneda) + '-' + str(self.fecha)
