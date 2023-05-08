from django.urls import path
from . import views



urlpatterns = [
    path('',views.home, name='home'),
    path('complete_task/',views.complete_task, name='complete_task'),
    path('create/', views.create_task, name='create'),  
    path('edit/<str:pk>/', views.edit_task, name='edit'),
    path('delete/<str:pk>/', views.delete_task, name='delete'),
]