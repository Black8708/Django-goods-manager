"""
URL configuration for management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from goods_app.views import black
from goods_app.views import add 
from goods_app.views import update
from goods_app.views import delete,filter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',black.as_view(),name='table_view'),
    path('add/',add.as_view(),name='goods'),
    path('update/<int:pk>',update.as_view(),name='update'),
    path('delete/<int:pk>/',delete,name='delete'),
    path("filter/",filter,name="table_filter")
   
    
]
