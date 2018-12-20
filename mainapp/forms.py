from django import forms
import datetime
from django.forms.extras.widgets import SelectDateWidget

from .models import Work, Device

class AddWork(forms.ModelForm):

    class Meta:
        model = Work
        fields = ('date', 'work_body',)
        widgets = {
           
            'date': forms.DateInput(attrs={'type': 'date', 'min':'2000-01-02', 'class':'form-control'}),
            'work_body': forms.Textarea(attrs={'class':'form-control'}),
        }


class AddDevice(forms.ModelForm):

    class Meta:
        model = Device
        fields = ('factory_number', 'device_type', 'factory_date', 'work_station','state','work_date','work_number',)
        # field1 = forms.DateField(widget=SelectDateWidget)
        widgets = {
            'factory_number': forms.NumberInput(attrs={'class':'form-control'}),
            'device_type': forms.Select(attrs={'class':'browser-default custom-select'}),
            'factory_date': forms.DateInput(attrs={'type': 'date', 'min':'2000-01-02', 'class':'form-control'}),
            'work_date': forms.DateInput(attrs={'type': 'date', 'min':'2000-01-02', 'class':'form-control', 'id':'work_date'}),
            'work_number': forms.TextInput(attrs={'class':'form-control', 'id':'work_number'}),
            'state': forms.Select(attrs={'class':'browser-default custom-select', 'id':'state', 'onclick':'disable()'}),
            'work_station':forms.Select(attrs={'class':'browser-default custom-select',}),
        }
