from django import forms
from chosun_utils.models import Todo, Scrap


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['content']


class ScrapForm(forms.ModelForm):
    class Meta:
        model = Scrap
        fields = ['title', 'url']