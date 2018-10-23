from django import forms
from .models import Comment

##using django Form
class EmailPostform(forms.Form):
	name = forms.CharField(max_length=25)
	emailfrom = forms.EmailField()
	to = forms.EmailField()
	comments = forms.CharField(required=False, widget=forms.Textarea)

##using ModelForm
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['name',
				  'email',
				  'body']