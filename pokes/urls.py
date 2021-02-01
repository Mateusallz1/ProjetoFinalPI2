from django.contrib import admin
from django.urls import path, include
from pokes import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#from rest_framework_swagger.views import get_swagger_view

#schema_view = get_swagger_view(title='Projeto Final Documentação')
schema_view = get_schema_view(
    openapi.Info(
        title="PokeResearch API",
        default_version='V1',
        description="API para um projeto de PI2",
        terms_of_service="https://www.google.com./policies/terms/",
        contact=openapi.Contact(email="trafalgarmateus@gmail.com"),
        license=openapi.License(name="Teste"),
    ),  
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('api_documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('pokes/', views.ListPokes.as_view(), name=views.ListPokes.name),
    path('pokes-detail/<int:pk>/', views.DetailPokes.as_view(), name=views.DetailPokes.name),
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