from django.urls import path

from . import views

app_name = 'userstories'
urlpatterns = [
    path('', views.index, name='index')
]