from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from purch_calculator.removal_rates.models import RemovalForSunflower
from purch_calculator.removal_rates.models import RemovalForRapeseed
from .forms import SunflowerForm , RapeseedForm

class ViewRates(ListView):
    model = RemovalForSunflower
    template_name = 'index.html'
    context_object_name = "sunflower_list"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        sunflower, _ = RemovalForSunflower.objects.get_or_create(pk=1)
        rapeseed, _ = RemovalForRapeseed.objects.get_or_create(pk=1)

        ctx["sunflower"] = sunflower
        ctx["raps"] = rapeseed
        return ctx

class UpdateSunflower(UpdateView):
    model = RemovalForSunflower
    form_class = SunflowerForm
    success_url = reverse_lazy('index')
    template_name = 'change_data/update_sunflower.html'

    def get_object(self, queryset=None):
        obj, _ = RemovalForSunflower.objects.get_or_create(pk=1)
        return obj


class UpdateRaps(UpdateView):
    model = RemovalForRapeseed
    form_class = RapeseedForm
    success_url = reverse_lazy('index')
    template_name = 'change_data/update_raps.html'

    def get_object(self, queryset=None):
        obj, _ = RemovalForRapeseed.objects.get_or_create(pk=1)
        return obj
# Create your views here.
