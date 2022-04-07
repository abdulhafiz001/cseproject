from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"), 
   path('propage/', views.propage, name="propage"),
   path('About/',views.About, name="About"),
   path('pro2/',views.pro2, name="pro2"),
   path('pro3/',views.pro3, name="pro3"),
   path('pro4',views.pro4, name="pro4"),
   path('shop',views.shop, name="shop"),
   path('account/',views.account, name="account"),
   path('pro',views.pro, name="pro"),
   path('index',views.index, name="index"),  
]