from django.db import models
from usuarios.models import Persona, AgenteLegal
from comprasServicios.models import Producto


class TipoProceso(models.Model):
	tipNombre = models.TextField(max_length = 140)
	tipDescricion = models.TextField(max_length = 300)
	proId = models.TextField(Producto)

	def __unicode__(self):
		return "Tipo Proceso: %s con producto %s" % (self.tipNombre, self.proId)

class Proceso(models.Model):
	proRadicado = models.TextField(max_length =  250)
	proAccionante = models.ForeignKey(Persona)
	#proAccionado = models.ForeignKey(Persona)
	ageId = models.ForeignKey(AgenteLegal)
	proFechaInicio = models.DateField(auto_now_add = True)
	proFechaFin = models.DateField()
	ESTADO = (
		('AC', 'Activo'),
		('DE', 'Desarrollo'),
		('FI', 'Finalizado'),
	)
	proEstado = models.TextField(max_length = 15, choices = ESTADO)
	#proReferencia = models.ForeignKey()
	proAsunto = models.TextField(max_length = 200)
	proContenido = models.TextField(max_length = 500)
	tipId = models.ForeignKey(TipoProceso)

	def __unicode__(self):
		return "Proceso con radicado %s" % (self.proRadicado,)

class DocumentoAdjunto(models.Model):
	docadNombre = models.CharField(max_length =  150)
	#docadAdjunto = models.FileField()
	proId = models.ForeignKey(Producto)

	def __unicode__(self):
		return "Nombre Adjunto: %s " % (self.atrib,)

class Notificacion(models.Model):
	proRadicado = models.ForeignKey(Proceso)
	notContenido = models.TextField(max_length = 500)
	docadId = models.ForeignKey(DocumentoAdjunto)
	PERMISOS_NOTIFICACION = (
		('ACN', 'Accionado'),
		('ACC', 'Accionante'),
		('A', 'Ambos'),
	)
	dirigidoA = models.TextField(max_length = 15, choices = PERMISOS_NOTIFICACION)

	def __unicode__(self):
		return 'Contenido %s ' % ( self.notContenido )

class Mensajero( models.Model ):
	menFechaIngreso = models.DateField( auto_now_add = True )
	menCobroPorEnvio = models.FloatField()

	def __unicode__(self):
		return "Cobro: %s" % self.menCobroPorEnvio

class Envio( models.Model ):
	proRadicado = models.ForeignKey( Proceso )
	perCedula = models.ForeignKey( Mensajero )
	envFecha = models.DateField( auto_now_add = True )

	def __unicode__(self):
		return "Fecha de envio: %s" % self.envFecha


