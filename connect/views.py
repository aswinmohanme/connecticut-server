from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .models import User
from django.forms.models import model_to_dict
from django.http import JsonResponse

from django.core import serializers

def user_view(request):
	form=UserForm()
	if request.method=='POST':
		form=UserForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
	y={
	  'form':form
	}
	return render(request,'user.html',y)

# Create your views here.
def get_view(request):
	id = request.GET.get('id')
	user = User.objects.get(mobile=id)
	user_data = model_to_dict(user, exclude=['photo'])
	user_data['photo'] = request.get_host() + user.photo.url

	return JsonResponse(user_data)