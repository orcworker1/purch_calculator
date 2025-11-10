from django.contrib import admin
from django.urls import path , include
from purch_calculator.removal_rates.views import ViewRates

urlpatterns = [
    path('',ViewRates.as_view(), name='view')
]
