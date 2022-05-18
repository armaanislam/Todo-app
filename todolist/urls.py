from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tasks'),
    path('update_tasks/<str:pk>/', views.updateTask, name='update_tasks'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
]