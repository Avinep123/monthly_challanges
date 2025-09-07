from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path(("<int:month>"),views.monthly_challanges_by_num),
    path(("<str:month>"),views.monthly_challanges,name="month-challange"),
    path("hi/hi",views.hello),
]