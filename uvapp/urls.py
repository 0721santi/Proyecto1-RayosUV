from django.urls import path
from . import views
urlpatterns = [
    path('', views.init),
    path('index.html', views.init),
    path('hello/<str:user>', views.hello),
    path('historial.html',views.historial)
]