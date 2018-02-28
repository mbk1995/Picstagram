from django.db import models
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class pictures(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	caption = models.CharField(max_length=1000, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	images= models.FileField()
	
		
	def __str__(self):
		return self.caption 
