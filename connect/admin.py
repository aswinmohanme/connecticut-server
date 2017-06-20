from django.contrib import admin
from .models import User
class RatingUser(admin.ModelAdmin):
	readonly_fields = ('date',)
admin.site.register(User,RatingUser)


# Register your models here.
