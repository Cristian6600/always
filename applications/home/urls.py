from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [

    path(
        '', 
        views.QHola.as_view(),
        name='publico',
    ),
    
    path(
        'contacto', 
        views.ContatoCreateView.as_view(),
        name='contacto',
    ),

]