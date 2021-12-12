from django import urls
from django.urls import path
from .views import DrinkList,DrinkDetail
urlpatterns=[
    path('',DrinkList.as_view(),name='drink_list'),
    path('<int:pk>/',DrinkDetail.as_view(),name='drink_detail')
]