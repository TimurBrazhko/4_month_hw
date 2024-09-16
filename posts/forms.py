from django import forms
from posts.models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class PostForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField(max_length=100)
    content = forms.CharField()

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'python':
            raise forms.ValidationError('Python title is not valid')
        else:
            return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower() == content.lower():
            raise forms.ValidationError('content and titile cant be same')
        else:
            return cleaned_data


class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'python':
            raise forms.ValidationError('Python title is not valid')
        else:
            return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower() == content.lower():
            raise forms.ValidationError('content and titile cant be same')
        else:
            return cleaned_data
