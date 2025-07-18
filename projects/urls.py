from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list, name='department_list'),
    path('department/<str:department_name>/', views.department_projects, name='department_projects'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
] 