from django import forms
from . import models


class VideoForm(forms.ModelForm):
    class Meta:
        model = models.Video
        fields = '__all__'
        widgets = {
            'file': forms.FileInput(attrs={'accept': 'video/*'}),
        }

class UploadForm(forms.Form):
    file = forms.FileField()
