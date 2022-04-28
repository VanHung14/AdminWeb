from django import forms
from home.models import People
class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = "__all__"

