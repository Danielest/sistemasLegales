from django.db import models
from usuarios.models import AgenteLegal

# Create your models here.

class Compra(models.Model):
	comFecha = models.DateField(auto_now_add = True)
	ageId = models.ForeignKey(AgenteLegal)

	def __unicode__(self):
		return self.comFecha

class Producto(models.Model):
	proDescripcion = models.CharField(max_length =  200)
	proNombre = models.TextField(max_length = 140)
	proPrecio = models.FloatField()
	proDuracion = models.IntegerField()
	comId = models.ForeignKey(Compra)

