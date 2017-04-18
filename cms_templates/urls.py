"""cms_templates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from cms_templates_app import views
from django.contrib.auth.views import logout, login

urlpatterns = [
    url(r'^$', views.barra, name="Muestra todas las direcciones guardadas"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/', logout, {'next_page':'/'}),
    url(r'^login/', login, {'template_name': 'registration/login.html'}),
    url(r'^annotated/$', views.barraAnnotated, name="Muestra direcciones guardadas con plantilla"),
    url(r'^annotated/(.+)', views.processAnnotated, name="Pagina del recurso con plantilla"),
    url(r'(.+)', views.process, name="Pagina del recurso"),
]