from django import forms

from app.models import MusicModel,MovieModel

class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieModel
        fields = "__all__"


class MusicForm(forms.ModelForm):
    class Meta:
        model = MusicModel
        fields = "__all__"

