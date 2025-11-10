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

class ViewRates(ListView):
    model = RemovalForSunflower
    template_name = 'index.html'
    context_object_name = "sunflower_list"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["rapeseed_list"] = RemovalForRapeseed.objects.all().order_by("id")
        return ctx

class UpdateSunflower(UpdateView):
    model = RemovalForSunflower
    fields = ["Moisture", "Weed_impurity", "Oil_impurity", "Oil_content", "KCHM", "Protein"]
    success_url = reverse_lazy('index')
    template_name = 'change_data/update_sunflower.html'

    def get_object(self, queryset=None):
        obj, _ = RemovalForSunflower.objects.get_or_create(pk=1)
        return obj


class UpdateRaps(UpdateView):
    model = RemovalForRapeseed
    fields = ["Moisture", "Weed_impurity", "Oil_impurity", "Oil_content", "KCHM", "Protein"]
    success_url = reverse_lazy('index')
    template_name = 'change_data/update_raps.html'

    def get_object(self, queryset=None):
        obj, _ = RemovalForSunflower.objects.get_or_create(pk=1)
        return obj

# Create your views here.
