from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)
from django.views import View
import pandas as pd
from django.http import HttpResponse

from purch_calculator.removal_rates.models import RemovalForSunflower
from purch_calculator.removal_rates.models import RemovalForRapeseed , RawMaterialBatch, Tariffs
from .forms import SunflowerForm , RapeseedForm , SunflowerBatchForm , TariffsForm

result = [1,2,3,4]


class ViewRates(ListView):
    model = RemovalForSunflower
    template_name = 'index.html'
    context_object_name = "sunflower_list"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        sunflower, _ = RemovalForSunflower.objects.get_or_create(pk=1)
        rapeseed, _ = RemovalForRapeseed.objects.get_or_create(pk=1)
        batch, _ = RawMaterialBatch.objects.get_or_create(pk=1)
        tariffs , _ = Tariffs.objects.get_or_create(pk=1)
        ctx["sunflower"] = sunflower
        ctx["raps"] = rapeseed
        ctx["batch"] = batch
        ctx['tariffs'] = tariffs
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


class UpdateDataByParty(UpdateView):
    model = RawMaterialBatch
    form_class = SunflowerBatchForm
    success_url = reverse_lazy('index')
    template_name = 'change_data/update_data_by_party.html'

    def get_object(self, queryset=None):
        obj, _ = RawMaterialBatch.objects.get_or_create(pk=1)
        return obj

class UpdateTariffs(UpdateView):
    model = Tariffs
    form_class = TariffsForm
    success_url = reverse_lazy('index')
    template_name = 'change_data/update_tariffs.html'

    def get_object(self, queryset=None):
        obj, _ = Tariffs.objects.get_or_create(pk=1)
        return obj


class ExportCSV(View):
    def get(self, request, *args, **kwargs):
        one = RemovalForRapeseed.objects.all().values()
        qs = RemovalForSunflower.objects.all().values()
        df = pd.DataFrame(list(qs))
        one = pd.DataFrame(list(one))
        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="purch_result.csv"'
        df.to_csv(path_or_buf=response, index=False, encoding="utf-8")
        one.to_csv(path_or_buf=response, index=False, encoding="utf-8")
        return response



# Create your views here.
