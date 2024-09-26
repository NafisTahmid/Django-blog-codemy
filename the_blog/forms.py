from .models import Post, Category
from django import forms

choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post_heading', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs=({'class':'form-control'})),
            'title_tag': forms.TextInput(attrs=({'class':'form-control'})),
            'author': forms.Select(attrs=({'class':'form-control'})),
            'category':forms.Select(choices=choice_list, attrs=({'class':'form-control'})),
            'body': forms.Textarea(attrs=({'class':'form-control'}))
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs=({'class':'form-control'})),
            'body': forms.Textarea(attrs=({'class':'form-control'}))
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields ='__all__'

        widgets = {
            'name': forms.TextInput(attrs=({'class':'form-control'}))
        }