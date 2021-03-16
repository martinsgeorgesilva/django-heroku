from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
import os
from django.views.static import serve as staticserve
from asset.views import *
from atelier.views import *
from django.conf.urls import include, url

from django.http import StreamingHttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'login/', auth_views.LoginView.as_view(template_name='asset/templates/login.html'), name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(template_name='asset/templates/login.html'), name='logout'),

    path(r'index/<int:id>', index, name='index'),
    #path(r'Ajax/', Ajax, name='Ajax'),
    #path(r'lastValueRealTimeChart/', lastValueRealTimeChart, name='lastValueRealTimeChart'),
    #path(r'mensal', mensal, name='mensal'),
    #path(r'VarialbleMonitored/', VarialbleMonitored, name='VarialbleMonitored'),
    path(r'', option, name='option'),
    path(r'conf', conf, name='conf'),
    path(r'import_csv', import_csv, name='import_csv'),
    path(r'export_csv/<int:id>', export_csv, name='export_csv'),
    path(r'project/', project, name='project'),
    path(r'section/<int:id>', section, name='section'),
    path(r'delete_measure', delete_measure, name='delete_measure'),

    ########atelier_dash
    path(r'atelier/', atelier, name='atelier'),
    path(r'reserva/', reserva, name='reserva'),
    path(r'finaliza/<int:id>', finaliza, name='finaliza'),
    path(r'galeria/', galeria, name='galeria'),
    
    #url(r'^configurate/', include('conf.urls'), name='configurate'),
    #url(r'^dashboard/', include('asset.urls'), name='dashboard'),


]

	