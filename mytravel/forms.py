__author__ = 'franklin'

from django.contrib.auth.models import User

from django import forms


class MyregistrationForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model= User
        fields = ('username','email','password')



def user_exist(self):
    try:
        User.objects.filter(username = self.cleaned_data['username'])
    except User.DoesNotExist:
        return self.cleaned_data['username']
    raise forms.ValidationError("User exist")
'''
    def save(self, commit=True):
        user =super(UserCreationForm,self).save(commit=False)
        user.email= self.cleaned_data["email"]
        user.password = self.cleaned_data["password"]

        user.is_active=True
        if commit:
            user.save()

        return user
'''