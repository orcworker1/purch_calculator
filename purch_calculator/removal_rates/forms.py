from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from purch_calculator.removal_rates.models import RemovalForRapeseed,RemovalForSunflower, RawMaterialBatch, Tariffs



class SunflowerForm(forms.ModelForm):
    class Meta:
        model = RemovalForSunflower
        fields = [
        "moisture_base", "moisture_removal",
        "weed_impurity_base", "weed_impurity_removal",
        "oil_impurity_base", "oil_impurity_removal",
        "oil_content_base", "oil_content_removal",
        "KCHM_base", "KCHM_removal",
        "protein_base", "protein_removal"
    ]
        widgets = {
            field: forms.NumberInput(attrs={'step': '1'})
            for field in fields
        }




class RapeseedForm(forms.ModelForm):
    class Meta:
        model = RemovalForRapeseed
        fields = [
        "moisture_base", "moisture_removal",
        "weed_impurity_base", "weed_impurity_removal",
        "oil_impurity_base", "oil_impurity_removal",
        "oil_content_base", "oil_content_removal",
        "KCHM_base", "KCHM_removal",
        "protein_base", "protein_removal"
    ]
        widgets = {
            field: forms.NumberInput(attrs={'step': '1'})
            for field in fields
        }


class SunflowerBatchForm(forms.ModelForm):
    class Meta:
        model = RawMaterialBatch
        fields = [
            'purchase_price', 'weight_actual', 'culture',
            'moisture_actual', 'weed_impurity_actual',
            'oil_impurity_actual', 'oil_content_actual',
            'KCHM_actual', 'protein_actual','receipt_start_date',
            'receipt_end_date','purchase_type','target_factory','partner_type','contract_type','transport_type',
            'agreement_type','delay_days',
        ]
        widgets = {
            'purchase_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '1,00',
                'placeholder': 'Введите базовую цену'
            }),
            'weight_actual': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '1,00',
                'placeholder': 'Введите вес в тоннах'
            }),
            'moisture_actual': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '1,00',
                'placeholder': '%'
            }),
            'weed_impurity_actual': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '1,00',
                'placeholder': '%'
            }),
            'oil_impurity_actual': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '1,00',
                'placeholder': '%'
            }),
            'oil_content_actual': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '1,00',
                'placeholder': '%'
            }),
            'KCHM_actual': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '1,00',
                'placeholder': '%'
            }),
            'protein_actual': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '1,00',
                'placeholder': '%'
            }),
            'culture': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выбери культуру'
            }),
            'receipt_start_date':forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Выбери Дату'
            }),
            'receipt_end_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Выбери Дату'
            }),
            'purchase_type': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Вид закупки'
            }),
            'target_factory':forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выбери завод'
            }),
            'partner_type':forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выбери партнера'
            }),
            'contract_type':forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выбери контракт'
            }),
            'transport_type':forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выбери транспорт'
            }),
            'agreement_type':forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выбери Соглашение'
            }),
            'delay_days':forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '1,00',
                'placeholder': 'Колличество дней отсрочки'

            })


        }

class TariffsForm(forms.ModelForm):
    class Meta:
        model = Tariffs
        fields = [
            'distance', 'tariff', 'storage_days',
            'acceptance_cost', 'storage_cost',
            'shipping_cost', 'natural_loss_pct',
        ]
        widgets = {
            'distance': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '1,00',
                'placeholder': 'Введите растояние'
            }),
            'tariff' : forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '1,00',
                'placeholder': 'Введите тариф'
            }),
            'storage_days' : forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '1,00',
                'placeholder': 'Введите срок хранения'
            }),
            'acceptance_cost': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '1,00',
                'placeholder': 'Введите cтоимость приемки'
            }),
            'storage_cost': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '1,00',
                'placeholder': 'Введите cтоимость хранения'
            }),
            'shipping_cost' : forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '1,00',
                'placeholder': 'Введите cтоимость отгрузки'
            }),
            'natural_loss_pct': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '1,00',
                'placeholder': 'Введите естественную убыль'
            }),

        }
