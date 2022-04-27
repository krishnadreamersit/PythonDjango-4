from django import forms
from app4_1.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('id', 'name', 'address')