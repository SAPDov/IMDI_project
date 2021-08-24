from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number','street_address')


