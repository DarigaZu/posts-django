from django import forms

from apps.likes.models import Like
from apps.posts.models import Post

class LikeForm(forms.ModelForm):
    post = forms.ModelChoiceField(queryset=Post.objects.all()) 

    class Meta:
        model = Like
        fields = ['post']  
