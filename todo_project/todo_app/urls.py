from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='todo-home'), # Format-> route, function(like flask)
]
