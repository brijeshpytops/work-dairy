from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('', dashboard_view, name ='dashboard_view'),
    path('tasks_view/', tasks_view, name='tasks_view'),
]
