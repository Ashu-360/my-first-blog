from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    vehicle_no = forms.CharField(max_length=30, required=True)
    mobile_no = forms.CharField(max_length=30, required=True)

    class Meta():
        model = User
        fields = ('vehicle_no', 'mobile_no',)
