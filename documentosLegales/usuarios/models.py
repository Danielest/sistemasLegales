from django.db import models

class Persona(models.Model):
	perNombre = models.TextField(max_length = 140, help_text="Ingrese el nombre del proceso a crear")
	perApellidos = models.TextField(max_length = 140)
	TIPOS_DOCUMENTO = (
		('CC', 'Cedula de Ciudania'),
		('NIT', 'NIT'),
		('TI', 'Tarjeta de identidad'),
		('CE', 'Cedula de extranjero'),
	)
	perTipoDocumento = models.CharField(max_length = 140, choices = TIPOS_DOCUMENTO, default = 'CC')
	perDocumento = models.CharField(max_length = 30)
	perDireccion = models.TextField(max_length = 200)
	perTelefono = models.CharField(max_length = 200)
	perEmail = models.EmailField(max_length = 70)
	perClave = models.CharField(max_length = 15)

	def __unicode__(self):
		return self.perNombre

class AgenteLegal(models.Model):
	ageClave = models.CharField(max_length = 15)
	ESTADOS = (
		('AC', 'Activo'),
		('IN', 'Inactivo'),
	)
	ageEstado = models.CharField(max_length = 15)

	def __unicode__(self):
		return self.ageEstado


