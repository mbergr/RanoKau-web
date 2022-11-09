from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from map import views as map_views
app_name = 'core'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #path('lo', views.login_view, name='login'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)