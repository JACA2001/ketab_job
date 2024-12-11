from django import forms
from .models import Staf

from django import forms
from .models import Staf

class UpdateStafForm(forms.ModelForm):
    class Meta:
        model = Staf
        fields = ['name', 'est_date', 'ville', 'province']  
