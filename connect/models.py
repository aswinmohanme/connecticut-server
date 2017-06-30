from django.db import models
class User(models.Model):
	user_name=models.CharField(max_length=30)
	photo=models.FileField()
	address=models.TextField()
	mobile=models.IntegerField()
	facebook=models.CharField(max_length=30)
	instagram=models.CharField(max_length=30)
	twitter=models.CharField(max_length=30)
	github=models.CharField(max_length=30)
	job_title=models.CharField(max_length=30)
	company=models.CharField(max_length=30)
	date=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.user_name
	
	

# Create your models here.
