from tkinter.font import names

from django.contrib import admin
from django.urls import path , include
from purch_calculator.removal_rates.views import ViewRates, UpdateSunflower, UpdateRaps

urlpatterns = [
    path('',ViewRates.as_view(), name='index'),
    path('change_sunflower/',UpdateSunflower.as_view(),name='update_sunflower'),
    path('change_raps/',UpdateRaps.as_view(),name='update_raps'),
]
