"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from chosun_utils import views

app_name = 'chosun_utils'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('chosun_calendar/', views.calendar, name='calendar'),
    path('chosun_notice/', views.notice, name='notice'),
    path('chosun_language/', views.language, name='language'),
    path('chosun_scholarship/', views.scholarship, name='scholarship'),
    path('chosun_ctl/', views.ctl, name='ctl'),
    path('chosun_program/', views.program, name='program'),
]
