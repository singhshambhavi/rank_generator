from rank_app.models import Details
from django import forms 
from django.core import validators 

class PostForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ('name', 'uuid', 'topic', 'score')

        widgets ={
            'name':forms.TextInput(attrs={ 'placeholder': 'Enter Name','required': True, 'size': 20}),
            'uuid':forms.NumberInput(attrs={ 'placeholder': 'Enter UUID', 'maxlength': 10000, 'required': True, 'size': 20}),
            'topic':forms.TextInput(attrs={ 'placeholder': 'Enter Topic','required': True, 'size': 20}),
            'score':forms.NumberInput(attrs={ 'placeholder': 'Enter Score', 'maxlength': 100, 'required': True, 'size': 20}),
       }