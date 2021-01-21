from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = {'first_name','middle_name','last_name','email','password','role','is_active'}
		widgets ={'password':forms.PasswordInput()}
