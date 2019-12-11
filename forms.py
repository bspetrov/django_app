from django import forms
from kleiner_specht.models import Releases

class ReleaseInput(forms.Form):
    artist = forms.CharField(max_length=300)
    release_name = forms.CharField(max_length=300)
    bpm = forms.CharField(max_length=300)
    release_date = forms.CharField(max_length=400)
    download_link = forms.CharField(max_length=500)

    def save(self):
        artist = self.cleaned_data['artist']
        release_name = self.cleaned_data['release_name']
        bpm = self.cleaned_data['bpm']
        release_date = self.cleaned_data['release_date']
        download_link = self.cleaned_data['download_link']
        new_release = Releases(artist=artist, release_name=release_name, bpm=bpm,
                         release_date=release_date, download_link=download_link)
        new_release.save()

