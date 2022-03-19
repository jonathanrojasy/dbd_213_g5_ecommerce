from django.urls import path

from . import views

app_name = 'productos'
urlpatterns = [
    path('', views.index, name='index'),
    path('demo', views.demo, name='demo'),
]