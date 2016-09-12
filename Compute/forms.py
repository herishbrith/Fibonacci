from django import forms

class NumberForm(forms.Form):

	nthNumber = forms.IntegerField(widget=forms.NumberInput(attrs={

		"placeholder": "Enter Number",
		"min": 1
	}))
