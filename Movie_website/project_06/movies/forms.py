from turtle import textinput
from django import forms
from .models import Movie

genre_choices = (('코미디','코미디'), ('러브코미디','러브코미디'), ('느와르','느와르'))

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label= 'title',
        widget= forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'maxlength' : 10,
                'placeholder' : '영화제목을 입력하세요',
            }
        )
    )
    audience = forms.CharField(
        label= 'audience',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'maxlength' : 8,
                'placeholder': '관객수',
            }
        )
    )
    release_date = forms.DateField(
        label = 'release_date',
        widget=forms.DateInput(
            attrs={
                'class' : 'form-control'
            }
        )
    )
    genre = forms.ChoiceField(choices= genre_choices)
    score = forms.IntegerField(
        label= 'score'        
    )
    poster_url = forms.URLField(
        label= 'poster_url'
    )
    class Meta:
        model = Movie
        fields = '__all__'