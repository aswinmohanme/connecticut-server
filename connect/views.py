from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .models import User
from django.forms.models import model_to_dict
from django.http import JsonResponse

from django.core import serializers

def user_view(request):
	if request.method=='GET':
		user = User()	

		if (len(User.objects.filter(mobile=request.GET.get('mobile'))) == 1):
			return HttpResponse('');

		user.address = ""
		user.job_title = request.GET.get('job') 
		user.company = request.GET.get('comp') 
		user.user_name = request.GET.get('name')
		user.mobile = request.GET.get('mobile')
		user.facebook = request.GET.get('fb')
		user.twitter = request.GET.get('tw')
		user.instagram = request.GET.get('insta')
		user.save()
	return HttpResponse('');

# Create your views here.
def get_view(request):
	id = request.GET.get('id')
	user = User.objects.get(mobile=id)
	user_data = model_to_dict(user, exclude=['photo'])

	return JsonResponse(user_data)