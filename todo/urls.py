from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_list_create),
    path('todos/<int:pk>/', views.todo_update_delete),
    path('todos/clear/', views.todo_clear_all),
]