from turtle import textinput
from django import forms
from .models import Movie, Comment


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
  
    description = forms.Textarea
    
    class Meta:
        model = Movie
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = 'content',