from django.urls import path
from . import views

urlpatterns = [
    # Add Task
    path('addTask/', views.addTask, name='addTask'),
    # Mark as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    # Mark as undone
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    # Edit feature
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    # Delete feature
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]