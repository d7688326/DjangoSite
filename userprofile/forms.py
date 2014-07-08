__author__ = 'franklin'
from django import forms
from models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('intro','photo')