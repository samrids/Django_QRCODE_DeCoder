from django import forms
from qrcode4e.models import UserImg


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = UserImg
        fields = ('image',)