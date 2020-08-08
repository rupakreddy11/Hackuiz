from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db.models.signals import post_save
		
class Challenges(models.Model):
	challenge_name = models.CharField(max_length=100)
	challenge_solution = models.CharField(max_length=100)
	challenge_score=models.IntegerField(default=0)

	def __str__(self):
		return self.challenge_name


class Hackuiz_Taker(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	challenge_name=models.ForeignKey(Challenges, on_delete=models.CASCADE,null=True)
	completed=models.BooleanField(default=False)
	taker_score=models.IntegerField(default=0)
	attempts=models.IntegerField(default=0)

	def __str__(self):
		return self.user.username

def create_taker(sender, **kwargs):
	if kwargs['created']:
		for i in range(1,35):
			p=Challenges.objects.get(id=i)
			taker=Hackuiz_Taker.objects.create(user=kwargs['instance'],challenge_name=p)


post_save.connect(create_taker, sender=User)




class Challenge_Flag(models.Model):
	chlg_ans=models.CharField(max_length=100)

class Chlng_taker(models.Model):
	user_flag=models.CharField(max_length=100)
	user=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

