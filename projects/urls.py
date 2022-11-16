from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'projects'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('new-project/', views.newProject, name='new-project'),
    #path('map/', views.map, name='map'),
    path('new-task/', views.newTask, name='new-task'),
    path('projects/', views.projects, name='new-task'),
    path('confirmation-new-project/', views.confirmation_newproject, name='confirmation-new-project')
]