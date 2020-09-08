from django.conf.urls import include, url
from django.urls import path, include
from .views import register

from . import views



urlpatterns = [
	#URL DE INICIO
    url(r'^$', views.inicio),
    #URL DE LOGIN - Registrar
    url('perris/login', views.login , name="login"),
    #URL DE Perros Disponibles
    url('perris/disponibles', views.perros_disponibles , name="perros_disponibles"),
    url('administrador',views.administrador_inicio, name="adm.inicio" ),
    #URL para agregar un nuevo post del perro_rescatado 
    path('agregar', views.new_post_perro, name='new_post_perro'),
    #URL para eliminar post 
    #Eliminar POST
    path('eliminar/<int:pk>', views.delete_post_perro, name='delete_post_perro'),
    #URL de detalles del post
    url(r'^perro/(?P<pk>[0-9]+)/$', views.detail_post_perro,name='detail_post_perro'),
    #URL Para editar un Post del Perro Rescatado 
    
    path('perro/<int:pk>/editar/', views.edit_post_perro, name='edit_post_perro'),

    url(r'^form/', views.form, name='form'),

    url(r'^register/', views.register, name= "register"),

]

