from django.urls import path
from . import views
urlpatterns = [
    path('', views.agregarLibro),
    path('crear', views.agregarLibro),
    path('course/<id>',views.mostrarLibro),
    path('course/<id>/delete',views.deleteLibro)
]
