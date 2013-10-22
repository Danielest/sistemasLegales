from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$','procesos.views.procesos', name='home'),
    url(r'^procesos$','procesos.views.procesos', name='procesos'),
    url(r'^historico$','procesos.views.historico', name='historico'),
    url(r'^clientes$','procesos.views.clientes', name='clientes'),
    url(r'^miperfil$','procesos.views.miPerfil', name='miPerfil'),
    url(r'^procesosendesarrollo$','procesos.views.procesosEnDesarrollo', name='procesosEnDesarrollo'),
    # url(r'^documentosLegales/', include('documentosLegales.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
