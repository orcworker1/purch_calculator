from http.client import responses
from os import write

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
from datetime import datetime

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
        csv_parts = []
        
        removal_sunflower = RemovalForSunflower.objects.all().values()
        if removal_sunflower.exists():
            df_sunflower = pd.DataFrame(list(removal_sunflower))
            column_mapping = {}
            for field in RemovalForSunflower._meta.fields:
                if hasattr(field, 'verbose_name'):
                    verbose_name = str(field.verbose_name) if field.verbose_name else None
                    if verbose_name and verbose_name != field.name:
                        column_mapping[field.name] = verbose_name
                if field.name == 'id' and 'id' not in column_mapping:
                    column_mapping[field.name] = 'ID'
            if column_mapping:
                df_sunflower.rename(columns=column_mapping, inplace=True)
            csv_parts.append("КОЭФФИЦИЕНТЫ ДЛЯ ПОДСОЛНЕЧНИКА")
            csv_parts.append(df_sunflower.to_csv(index=False, encoding="utf-8-sig"))
        
        removal_rapeseed = RemovalForRapeseed.objects.all().values()
        if removal_rapeseed.exists():
            df_rapeseed = pd.DataFrame(list(removal_rapeseed))
            column_mapping = {}
            for field in RemovalForRapeseed._meta.fields:
                if hasattr(field, 'verbose_name'):
                    verbose_name = str(field.verbose_name) if field.verbose_name else None
                    if verbose_name and verbose_name != field.name:
                        column_mapping[field.name] = verbose_name
                if field.name == 'id' and 'id' not in column_mapping:
                    column_mapping[field.name] = 'ID'
            if column_mapping:
                df_rapeseed.rename(columns=column_mapping, inplace=True)
            csv_parts.append("КОЭФФИЦИЕНТЫ ДЛЯ РАПСА")
            csv_parts.append(df_rapeseed.to_csv(index=False, encoding="utf-8-sig"))
        
    
        raw_material_batch = RawMaterialBatch.objects.all().values()
        if raw_material_batch.exists():
            df_batches = pd.DataFrame(list(raw_material_batch))
            column_mapping = {}
            manual_mapping = {
                'id': 'ID',
                'culture': 'Культура',
                'purchase_type': 'Вид закупки',
                'target_factory': 'Целевой завод',
                'partner_type': 'Тип партнера',
                'contract_type': 'Тип контракта',
                'transport_type': 'Тип ТС',
                'agreement_type': 'Соглашение',
            }
            for field in RawMaterialBatch._meta.fields:
                if field.name in manual_mapping:
                    column_mapping[field.name] = manual_mapping[field.name]
                elif hasattr(field, 'verbose_name'):
                    verbose_name = str(field.verbose_name) if field.verbose_name else None
                    if verbose_name and verbose_name != field.name:
                        column_mapping[field.name] = verbose_name
            if column_mapping:
                df_batches.rename(columns=column_mapping, inplace=True)
           
            if not df_batches.empty:
                culture_map = dict(RawMaterialBatch.CULTURE_CHOICES)
                purchase_type_map = dict(RawMaterialBatch.PURCHASE_TYPE_CHOICES)
                factory_map = dict(RawMaterialBatch.FACTORY_CHOICES)
                partner_type_map = dict(RawMaterialBatch.PARTNER_TYPE_CHOICES)
                contract_type_map = dict(RawMaterialBatch.CONTRACT_TYPE_CHOICES)
                transport_type_map = dict(RawMaterialBatch.TRANSPORT_CHOICES)
                agreement_type_map = dict(RawMaterialBatch.AGREEMENT_CHOICES)
                

                if 'Культура' in df_batches.columns:
                    df_batches['Культура'] = df_batches['Культура'].map(culture_map).fillna(df_batches['Культура'])
                elif 'culture' in df_batches.columns:
                    df_batches['culture'] = df_batches['culture'].map(culture_map).fillna(df_batches['culture'])
                
                if 'Вид закупки' in df_batches.columns:
                    df_batches['Вид закупки'] = df_batches['Вид закупки'].map(purchase_type_map).fillna(df_batches['Вид закупки'])
                elif 'purchase_type' in df_batches.columns:
                    df_batches['purchase_type'] = df_batches['purchase_type'].map(purchase_type_map).fillna(df_batches['purchase_type'])
                
                if 'Целевой завод' in df_batches.columns:
                    df_batches['Целевой завод'] = df_batches['Целевой завод'].map(factory_map).fillna(df_batches['Целевой завод'])
                elif 'target_factory' in df_batches.columns:
                    df_batches['target_factory'] = df_batches['target_factory'].map(factory_map).fillna(df_batches['target_factory'])
                
                if 'Тип партнера' in df_batches.columns:
                    df_batches['Тип партнера'] = df_batches['Тип партнера'].map(partner_type_map).fillna(df_batches['Тип партнера'])
                elif 'partner_type' in df_batches.columns:
                    df_batches['partner_type'] = df_batches['partner_type'].map(partner_type_map).fillna(df_batches['partner_type'])
                
                if 'Тип контракта' in df_batches.columns:
                    df_batches['Тип контракта'] = df_batches['Тип контракта'].map(contract_type_map).fillna(df_batches['Тип контракта'])
                elif 'contract_type' in df_batches.columns:
                    df_batches['contract_type'] = df_batches['contract_type'].map(contract_type_map).fillna(df_batches['contract_type'])
                
                if 'Тип ТС' in df_batches.columns:
                    df_batches['Тип ТС'] = df_batches['Тип ТС'].map(transport_type_map).fillna(df_batches['Тип ТС'])
                elif 'transport_type' in df_batches.columns:
                    df_batches['transport_type'] = df_batches['transport_type'].map(transport_type_map).fillna(df_batches['transport_type'])
                
                if 'Соглашение' in df_batches.columns:
                    df_batches['Соглашение'] = df_batches['Соглашение'].map(agreement_type_map).fillna(df_batches['Соглашение'])
                elif 'agreement_type' in df_batches.columns:
                    df_batches['agreement_type'] = df_batches['agreement_type'].map(agreement_type_map).fillna(df_batches['agreement_type'])
            
            csv_parts.append("ВХОДНЫЕ ДАННЫЕ ПО ТЕКУЩЕЙ ПАРТИИ")
            csv_parts.append(df_batches.to_csv(index=False, encoding="utf-8-sig"))
        
       
        tariffs = Tariffs.objects.all().values()
        if tariffs.exists():
            df_tariffs = pd.DataFrame(list(tariffs))
            column_mapping = {}
            for field in Tariffs._meta.fields:
                if hasattr(field, 'verbose_name'):
                    verbose_name = str(field.verbose_name) if field.verbose_name else None
                    if verbose_name and verbose_name != field.name:
                        column_mapping[field.name] = verbose_name
                if field.name == 'id' and 'id' not in column_mapping:
                    column_mapping[field.name] = 'ID'
            if column_mapping:
                df_tariffs.rename(columns=column_mapping, inplace=True)
            csv_parts.append("ТАРИФЫ")
            csv_parts.append(df_tariffs.to_csv(index=False, encoding="utf-8-sig"))
        
        
        csv_content = "\n".join(csv_parts)
        
  
        response = HttpResponse(csv_content.encode('utf-8-sig'), content_type='text/csv; charset=utf-8-sig')
        
        date_str = datetime.now().strftime('%Y%m%d_%H%M%S')
        response['Content-Disposition'] = f'attachment; filename="export_{date_str}.csv"'
        
        return response



# Create your views here.
