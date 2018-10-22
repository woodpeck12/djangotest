from django import forms

class EmailPostform(forms.Form):
	name = forms.CharField(max_length=25)
	emailfrom = forms.EmailField()
	to = forms.EmailField()
	comments = forms.CharField(required=False, widget=forms.Textarea)

