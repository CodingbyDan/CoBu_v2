from django import forms
from .models import Post, Category


choices = Category.objects.all().values_list('name', 'name')


choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'platform', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 
                'placeholder': 'Enter a title..'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 
                'placeholder': 'Enter game title..'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 
                'value': '', 'id': 'user', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, 
                attrs={'class': 'form-control'}),
            'platform': forms.Select(choices=Post.PLATFORM_CHOICES, 
                attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 
                'placeholder': 'Enter a title..'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 
                'placeholder': 'Enter game title..'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }