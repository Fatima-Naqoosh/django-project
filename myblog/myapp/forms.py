
from django import forms
from .models import Destination


class MyForm(forms.ModelForm):
    title = forms.CharField()
    img = forms.ImageField()
    desc = forms.Textarea()

    class Meta:
        model = Destination
        fields = ['title', 'img', 'desc']
