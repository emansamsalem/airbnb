from django.urls import path
from . import views


app_name = 'property'

urlpatterns = [
    path('', views.PropertyList.as_view(), name= 'property_list1'),
    path('<slug:slug>', views.PropertyDetail.as_view(), name = 'property_detail1'),

    ]