from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
import os
from django.views.static import serve as staticserve
from asset.views import *

urlpatterns = [


    path(r'view/', view, name='view'),



]
