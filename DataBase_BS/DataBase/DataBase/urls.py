"""DataBase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from database_app import views
from django.conf.urls import url

urlpatterns = [
    url('admin/', admin.site.urls),
    url('index/', views.Index),
    url(r'json/', views.getJson),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^search_score/(.*?)$', views.search_score),
    url(r'^search_course/(.*?)$', views.search_course),
    url(r'^choose_course/$', views.choose_course),
    url(r'^drop_course/$', views.drop_course),
    url(r'^t_login/$', views.t_login),
    url(r'^t_course/$', views.t_course),
    url(r'^t_course_detal/(.*?)/(.*?)/(.*?)$', views.t_course_detal),
    url(r'^t_course_mark/(.*?)/(.*?)/(.*?)$', views.t_course_mark),
]
