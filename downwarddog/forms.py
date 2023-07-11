from .models import Comment
from django import forms
from .models import Booking


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
