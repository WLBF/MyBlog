from django import forms
from wlbf.models import Blog, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)


class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the blog.")
    content = forms.CharField(widget=forms.Textarea, help_text="Please enter the content of the blog.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Blog

        exclude = ('category',)
