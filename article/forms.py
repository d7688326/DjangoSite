__author__ = 'franklin'
from django import forms
from models import Article,Comment,Procedure


class ArticleForm(forms.ModelForm):
    title= forms.CharField(max_length=200,label='Name of your recipe')
    materials = forms.CharField(max_length=200,label='What should I prepare')
    class Meta:
        model= Article
        #fields to be added
        fields = ('title','materials','cooktime','difficulty','steps','body','thumbnail')

class CommentForm(forms.ModelForm):

    class Meta:
        model= Comment
        fields = ('body','rating')

class ProcedureForm(forms.ModelForm):

    class Meta:
        model = Procedure
        fields = ('description','picture')

class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)

class ContactForm2(forms.Form):
    sender = forms.EmailField()

class ContactForm3(forms.Form):
    message = forms.CharField(widget=forms.Textarea)

