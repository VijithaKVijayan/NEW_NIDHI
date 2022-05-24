"""EMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from xml.dom.minidom import Document
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from CMS import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('login', views.login, name='login'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('adminregister', views.adminregister, name='adminregister'),
    path('search', views.search, name='search'),
    path('cusdetails',views.cusdetails, name='cusdetails'),
    path('verify',views.verify, name='verify'),
    path('leveloneregistration',views.leveloneregistration, name='leveloneregistration'),
    path('levelonelogin',views.levelonelogin, name='levelonelogin'),
    path('leveltworegistration',views.leveltworegistration, name='leveltworegistration'),
    path('leveltwologin',views.leveltwologin, name='leveltwologin'),
    path('levelthreeregistration',views.levelthreeregistration, name='levelthreeregistration'),
    path('levelthreelogin',views.levelthreelogin, name='levelthreelogin'),
    path('show',views.show,name='show'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('admmain',views.admmain, name='admmain'),
    path('adminview', views.adminview, name='adminview'),
    path('adminedit/<int:id>', views.adminedit, name='adminedit'),
    path('adminupdate/<int:id>', views.adminupdate, name='adminupdate')


]
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)