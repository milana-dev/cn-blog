from django import forms

from blogs.models import Blog


class BlogForm(forms.ModelForm):
    published_date = forms.DateTimeField(input_formats=['%d-%m-%Y %H:%M'], required=False)
    class Meta:
        model = Blog
        exclude = ('author',)
        # bunu hemcinin belede yazmaq olar fields = ('title', 'about', 'published_date')


