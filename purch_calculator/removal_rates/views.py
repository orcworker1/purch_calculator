from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from purch_calculator.removal_rates.models import Removal

class ViewRates(ListView):
    model = Removal
    template_name = 'index.html'
    context_object_name = 'rates'

# Create your views here.
