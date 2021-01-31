from django.contrib import admin
from django.urls import path, include
from pokes import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),

    path('pokes/', views.ListPokes.as_view(), name=views.ListPokes.name),
    path('poke-detail/<int:pk>/', views.DetailPokes.as_view(), name=views.DetailPokes.name),
    path('trainers/', views.ListTrainers.as_view(), name=views.ListTrainers.name),
    path('trainers-detail/<int:pk>/', views.DetailTrainers.as_view(), name=views.DetailTrainers.name),
    path('types/', views.ListTypes.as_view(), name=views.ListTypes.name),
    path('types-detail/<int:pk>/', views.DetailTypes.as_view(), name=views.DetailTypes.name),
    path('researchers/', views.ListResearchers.as_view(), name=views.ListResearchers.name),
    path('researchers-detail/<int:pk>/', views.DetailResearchers.as_view(), name=views.DetailResearchers.name),
    path('users/', views.ListUsers.as_view(), name=views.ListUsers.name),
    path('users-detail/', views.DetailUsers.as_view(), name=views.DetailUsers.name),
    path('api-auth/', include('rest_framework.urls')),
]