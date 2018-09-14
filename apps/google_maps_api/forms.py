from django import forms

class TripForm(forms.Form):
    starting_address = forms.CharField(label='Starting Address', max_length=125)
    ending_address = forms.CharField(label='Ending Address', max_length=125)