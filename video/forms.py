from django import forms

from . import models

class VideoForm(forms.ModelForm):
    class Meta:
        model = models.VideoModel
        fields = '__all__'