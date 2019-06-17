# from django import forms
from django.forms import ModelForm
from second.models import Post
from django.utils.translation import gettext_lazy as _

class PostForm(ModelForm):
    class Meta:
        model= Post
        fields=['title', 'content']
        labels={
            'title':_('제목'),
            'content':_('내용'),
        }
        help_texts={
            'title':_('input title'),
            'content':_('input content'),
        }

# class PostForm(forms.Form):
#     title= forms.CharField(label='title', max_length=200)
#     content= forms.CharField(label='content',widget= forms.Textarea)