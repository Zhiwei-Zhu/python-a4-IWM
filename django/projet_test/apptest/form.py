import imp
from pyexpat import model
from django import forms
from .models import Questions

class QuestionForms(forms.ModelForm):

    class Meta:

        model = Questions

        fields = ["text"]