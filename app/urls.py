
from django.urls import path
from .views import *

urlpatterns = [
    # views logic 
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('dashboard/', Userdashboard, name="dashboard"),
    path('cluster_dashboard/', Clusterdashboard, name="cluster_dashboard"),




    

    # control logic 




]