from django import forms
from wlbf.models import Blog, Category, UserProfile
from django.contrib.auth.models import User



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
    title = forms.CharField(max_length=128)
    content = forms.CharField(widget=forms.Textarea)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    post_time = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    update_time = forms.DateTimeField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Blog

        exclude = ('category',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
