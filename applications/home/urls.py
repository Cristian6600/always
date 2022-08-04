from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [

    path(
        'e', 
        views.QHola.as_view(),
        name='publico',
    ),

]