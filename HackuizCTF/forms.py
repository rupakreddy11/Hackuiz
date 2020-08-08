from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Hackuiz_Taker, Chlng_taker
from django import forms
from django.forms import ModelForm

class SignupForm(UserCreationForm):
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
	first_name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'first_name','last_name', 'email', 'password1', 'password2',)

	def __init__(self, *args, **kwargs):
	    super(SignupForm, self).__init__(*args, **kwargs)

	    self.fields['username'].widget.attrs['class'] = 'form-control'
	    self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
	    
	    self.fields['password1'].widget.attrs['class']='form-control'
	    self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
	    
	    self.fields['password2'].widget.attrs['class']='form-control'
	    self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before,for verification.</small></span>'


class AnswerForm(forms.ModelForm):
	flag=forms.CharField(max_length=100)

	class Meta:
		model=Hackuiz_Taker
		fields={'user','challenge_name','completed','taker_score','attempts',}