from django import forms
from api.models import *
from django.contrib.auth.models import User

class transForms(forms.Form):
    date = forms.DateField(widget=forms.widgets.NumberInput(attrs={'type': 'date','class':'form-control','id':'date'}))
    amount = forms.DecimalField(widget=forms.widgets.NumberInput(attrs={'class':'form-control','id':'amount'}))
    paidby = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.widgets.Select(attrs={'class':'form-control','id':'paidby'}))
    member = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    category = forms.ModelChoiceField(queryset = Category.objects.all(),widget=forms.widgets.Select(attrs={'class':'form-control','id':'category'}))

    class Meta:
        model = TranscationsData
        fields = ['date','paidby','amount','member','category']