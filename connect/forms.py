from django import forms
from .models import User
class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['user_name','photo','mobile','address','facebook','instagram','twitter','github','job_title','company']