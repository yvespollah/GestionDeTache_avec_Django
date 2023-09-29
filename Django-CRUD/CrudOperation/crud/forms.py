from django import forms
from .models import Tache

class FormTache(forms.ModelForm):
    tache = forms.CharField(max_length=200,widget=forms.TextInput(attrs={
        'placeholder':'Entrer votre tache',
        'class':'form-control-lg',
    }))
    
    class Meta:
        model = Tache
        fields = ['tache']
