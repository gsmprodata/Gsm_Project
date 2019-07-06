from django.contrib import admin
from django.urls import path
# import home.views
import home.views

urlpatterns = [
    path('',home.views.landing,name='home'),
    path('<str:brand>/',home.views.brandinfo,name = "brandinfo"),
    path('pro/<int:pro_id>/',home.views.prodetail,name='prodetail'),
    path('search_phone',home.views.search_phone,name='search_phone'),
]
