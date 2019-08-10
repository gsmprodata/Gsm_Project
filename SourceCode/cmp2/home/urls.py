from django.contrib import admin
from django.urls import path
# import home.views
import home.views

urlpatterns = [
    path('',home.views.landing,name='home'),#Check
    path('<str:brand>/',home.views.brandinfo,name = "brandinfo"),
    path('pro/<int:pro_id>/',home.views.prodetail,name='prodetail'),
    path('search_phone',home.views.search_phone,name='search_phone'),
    path('compare_phone/<int:phone1>/<int:phone2>/',home.views.compare_phone,name='compare_phone'),
    path('compare_phone/',home.views.compare_phone,name='compare_phone_string'),
]
