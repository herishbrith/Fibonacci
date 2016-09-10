from django import forms

class NumberForm(forms.Form):

	nthNumber = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Nth Number"}))
