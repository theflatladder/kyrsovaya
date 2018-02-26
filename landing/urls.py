from django.conf.urls import url,include
from django.contrib import admin
from landing import views

urlpatterns = [
    url(r'^login/', views.login, name='landing'),
    url(r'^reg/', views.reg, name='landing'),
    url(r'^main/', views.main, name='landing'),
    url(r'^logout/', views.logout, name='landing')
]