from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from purch_calculator.removal_rates.models import RemovalForRapeseed,RemovalForSunflower



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