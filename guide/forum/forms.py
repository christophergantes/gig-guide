from django import forms

from .models import ForumPost


class ForumForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ["title", "content", "category"]
