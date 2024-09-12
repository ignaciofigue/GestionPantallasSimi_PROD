from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('datosTote', views.datosTote, name='datosTote'),
    path('salida01', views.salida01, name='salida01'),
    path('salida02', views.salida02, name='salida02'),
    path('salida03', views.salida03, name='salida03'),
    path('salida04', views.salida04, name='salida04'),
    path('salida05', views.salida05, name='salida05'),
    path('destinos', views.destinos, name='destinos'),
    path('home', views.landingPage, name='home'),
    path('ripley', views.ripley, name='ripley'),
    path('limpiarbbdd', views.limpiar_bbdd, name='limpiarbbdd'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

