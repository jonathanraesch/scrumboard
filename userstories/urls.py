from django.urls import path

from . import views

app_name = 'userstories'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:story_id>/delete', views.delete_story, name='delete_story'),
    path('<int:story_id>/', views.detail, name='detail'),
]
