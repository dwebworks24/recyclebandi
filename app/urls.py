
from django.urls import path
from .views import *

urlpatterns = [
    # views logic 
    path('', Commingsoon, name="commingsoon"),
    path('home/', home, name="home"),
    path('about/', about, name="about"),
    path('price_list/', price_list, name="price_list"),
    path('papers/', papers, name="papers"),
    path('plastic/', plastic, name="plastic"),
    path('old_cloth/', old_cloth, name="old_cloth"),
    path('dore_to_dore/', dore_to_dore, name="dore_to_dore"),
    path('mixed_wast/', mixed_wast, name="mixed_wast"),
    path('metals/', metals, name="metals"),
    path('contact/', contact, name="contact"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('dashboard/', Userdashboard, name="dashboard"),
    path('cluster_dashboard/', Clusterdashboard, name="cluster_dashboard"),
    path('new_shop_owner/', New_customer, name="new_shop_owner"),




    

    # control logic 




]