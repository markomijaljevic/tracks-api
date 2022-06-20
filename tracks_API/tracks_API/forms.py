from django import forms
from . import models

class CreateTrackForm(forms.ModelForm):
    class Meta:
        model = models.Tracks
        fields = [
            "title",
            "artist",
            "duration",
            "last_play",
        ]