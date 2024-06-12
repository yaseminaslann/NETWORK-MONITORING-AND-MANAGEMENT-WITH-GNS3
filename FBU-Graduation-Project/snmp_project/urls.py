from django.contrib import admin
from django.urls import path
from snmp_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.userlogin, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutuser, name='logout'),
    path('devicelist/', views.devicelist, name='devicelist'),


]
