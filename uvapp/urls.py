from django.urls import path
from . import views
urlpatterns = [
    path('', views.init),
    path('index.html', views.init),
    path('backend/inicio.html', views.login),
    path('backend/registro.html', views.singup),
    path('loggedin.html', views.reguser),
    path('backend/historial.html',views.historial)
]