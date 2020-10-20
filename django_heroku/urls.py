from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
import os
from django.views.static import serve as staticserve
from asset.views import *
from django.conf.urls import include, url

from django.http import StreamingHttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'login/', auth_views.LoginView.as_view(template_name='asset/templates/login.html'), name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(template_name='asset/templates/login.html'), name='logout'),

    path(r'index', index, name='index'),
    path(r'index_1', index_1, name='index_1'),
    #path(r'Ajax/', Ajax, name='Ajax'),
    #path(r'lastValueRealTimeChart/', lastValueRealTimeChart, name='lastValueRealTimeChart'),
    #path(r'mensal', mensal, name='mensal'),
    #path(r'VarialbleMonitored/', VarialbleMonitored, name='VarialbleMonitored'),
    path(r'', option, name='option'),
    path(r'conf', conf, name='conf'),


    #url(r'^configurate/', include('conf.urls'), name='configurate'),
    #url(r'^dashboard/', include('asset.urls'), name='dashboard'),


]

	