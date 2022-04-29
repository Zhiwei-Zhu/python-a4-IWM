import imp
from django import forms
from .models import  Room

class RoomForms(forms.ModelForm):

    class Meta:

        model = Room

        fields = ["name"]