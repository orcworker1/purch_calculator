from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from purch_calculator.removal_rates.models import RemovalForRapeseed,RemovalForSunflower



class SunflowerForm(forms.ModelForm):
    class Meta:
        model = RemovalForSunflower
        fields = ["Moisture", "Weed_impurity", "Oil_impurity", "Oil_content", "KCHM", "Protein"]

class RapeseedForm(forms.ModelForm):
    class Meta:
        model = RemovalForRapeseed
        fields = ["Moisture", "Weed_impurity", "Oil_impurity", "Oil_content", "KCHM", "Protein"]