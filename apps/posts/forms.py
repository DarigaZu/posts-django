from django import forms

from apps.posts.models import Post

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description', 'image'] 

class PostUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description']        