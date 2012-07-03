from django import forms

class PodcastsForm(forms.Form):
    name = forms.CharField(max_length=25)
    rss = forms.TestField()
    