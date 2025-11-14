from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from purch_calculator.removal_rates.models import RemovalForRapeseed,RemovalForSunflower, RawMaterialBatch



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
            'KCHM_actual', 'protein_actual'
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

        }