from django.urls import path

from .views import *

app_name = 'car'
urlpatterns = [
    path('car/create/', CarCreateView.as_view(), name='create_car'),
    path('car/list/', CarListView.as_view(), name='car_list'),
    path('car/detail/<int:pk>', CarDetailView.as_view(), name='car_detail')
] 
