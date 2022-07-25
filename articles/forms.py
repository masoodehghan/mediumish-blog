from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image', 'tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form-input'})
        }
