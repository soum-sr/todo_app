from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='todo-home'), # Format-> route, function(like flask)
    path('update/<str:pk>/',views.updateTask, name="update"),
    path('delete/<str:pk>/',views.deleteTask, name="delete"),
]
