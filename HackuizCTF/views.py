from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, AnswerForm
from django.contrib.auth.decorators import login_required
from .models import Challenges, Hackuiz_Taker, Challenge_Flag
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum

def home(request):
	if request.user.is_authenticated:
		p=Hackuiz_Taker.objects.filter(user=request.user)
		ts=p.aggregate(Sum('taker_score'))['taker_score__sum']
		return render(request, 'HackuizCTF/index.html', {'p':ts})
	else:
		return render(request,'HackuizCTF/index.html',{})

		
def User_login(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password= password)
		if user is not None:
			login(request, user)
			messages.success(request, 'You have successfully logged In!!!')
			return redirect('home')
		else:
			messages.success(request, 'Invalid credentials, Try again...')
			return redirect('login')
	else:
		return render(request, 'HackuizCTF/login.html', {})

def User_logout(request):
	logout(request)
	messages.success(request, 'You have been logged out!!!')
	return redirect('home')

def register(request):
	if request.method=='POST':
		form=SignupForm(request.POST)
		if form.is_valid():
			form.save()
			username=request.POST['username']
			password=request.POST['password1']
			user=authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request, 'You have successfully registered for Hackuiz..!!!')
			return redirect('home')
	else:
		form=SignupForm()
		
	context = {'form' : form}
	return render(request, 'HackuizCTF/signup.html', context)




@login_required(login_url="/list/login")
def challenges(request):
	return render(request, 'HackuizCTF/list.html', {})

@login_required(login_url="/list/login")
def chlg_101(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=1)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=1)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/101.html', context)
	else:
		return render(request,'HackuizCTF/101.html',{})

@login_required(login_url="/list/login")
def chlg_102(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=2)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=2)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, "You have captured the flag successfully!!!")
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/102.html', context)
	else:
		return render(request,'HackuizCTF/102.html',{})

@login_required(login_url="/list/login")
def chlg_103(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=3)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=3)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/103.html', context)
	else:
		return render(request,'HackuizCTF/103.html',{})

@login_required(login_url="/list/login")
def chlg_104(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=4)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=4)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/104.html', context)
	else:
		return render(request,'HackuizCTF/104.html',{})

@login_required(login_url="/list/login")
def chlg_105(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=5)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=5)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/105.html', context)
	else:
		return render(request,'HackuizCTF/105.html',{})

@login_required(login_url="/list/login")
def chlg_106(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=6)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=6)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/106.html', context)
	else:
		return render(request,'HackuizCTF/106.html',{})

@login_required(login_url="/list/login")
def chlg_107(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=7)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=7)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/107.html', context)
	else:
		return render(request,'HackuizCTF/107.html',{})

@login_required(login_url="/list/login")
def chlg_108(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=8)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=8)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/108.html', context)
	else:
		return render(request,'HackuizCTF/108.html',{})

@login_required(login_url="/list/login")
def chlg_109(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=9)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=9)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/109.html', context)
	else:
		return render(request,'HackuizCTF/109.html',{})

@login_required(login_url="/list/login")
def chlg_110(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=10)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=10)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/110.html', context)
	else:
		return render(request,'HackuizCTF/110.html',{})

@login_required(login_url="/list/login")
def chlg_111(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=11)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=11)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/111.html', context)
	else:
		return render(request,'HackuizCTF/111.html',{})

@login_required(login_url="/list/login")
def chlg_112(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=12)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=12)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/112.html', context)
	else:
		return render(request,'HackuizCTF/112.html',{})

@login_required(login_url="/list/login")
def chlg_113(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=13)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=13)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/113.html', context)
	else:
		return render(request,'HackuizCTF/113.html',{})

@login_required(login_url="/list/login")
def chlg_114(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=14)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=14)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/114.html', context)
	else:
		return render(request,'HackuizCTF/114.html',{})

@login_required(login_url="/list/login")
def chlg_115(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=15)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=15)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/115.html', context)
	else:
		return render(request,'HackuizCTF/115.html',{})

@login_required(login_url="/list/login")
def chlg_116(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=16)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=16)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/116.html', context)
	else:
		return render(request,'HackuizCTF/116.html',{})

@login_required(login_url="/list/login")
def chlg_117(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=17)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=17)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/117.html', context)
	else:
		return render(request,'HackuizCTF/117.html',{})

@login_required(login_url="/list/login")
def chlg_118(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=18)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=18)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/118.html', context)
	else:
		return render(request,'HackuizCTF/118.html',{})

@login_required(login_url="/list/login")
def chlg_119(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=19)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=19)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/119.html', context)
	else:
		return render(request,'HackuizCTF/119.html',{})

@login_required(login_url="/list/login")
def chlg_120(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=20)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=20)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/120.html', context)
	else:
		return render(request,'HackuizCTF/120.html',{})

@login_required(login_url="/list/login")
def chlg_121(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=21)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=21)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/121.html', context)
	else:
		return render(request,'HackuizCTF/121.html',{})

@login_required(login_url="/list/login")
def chlg_122(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=22)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=22)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/122.html', context)
	else:
		return render(request,'HackuizCTF/122.html',{})

@login_required(login_url="/list/login")
def chlg_123(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=23)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=23)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/123.html', context)
	else:
		return render(request,'HackuizCTF/123.html',{})

@login_required(login_url="/list/login")
def chlg_124(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=24)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=24)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/124.html', context)
	else:
		return render(request,'HackuizCTF/124.html',{})

@login_required(login_url="/list/login")
def chlg_125(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=25)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=25)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/125.html', context)
	else:
		return render(request,'HackuizCTF/125.html',{})

@login_required(login_url="/list/login")
def chlg_126(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=26)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=26)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/126.html', context)
	else:
		return render(request,'HackuizCTF/126.html',{})

@login_required(login_url="/list/login")
def chlg_127(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=27)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=27)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/127.html', context)
	else:
		return render(request,'HackuizCTF/127.html',{})

@login_required(login_url="/list/login")
def chlg_128(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=28)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=28)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/128.html', context)
	else:
		return render(request,'HackuizCTF/128.html',{})

@login_required(login_url="/list/login")
def chlg_129(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=29)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=29)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/129.html', context)
	else:
		return render(request,'HackuizCTF/129.html',{})

@login_required(login_url="/list/login")
def chlg_130(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=30)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=30)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/130.html', context)
	else:
		return render(request,'HackuizCTF/130.html',{})

@login_required(login_url="/list/login")
def chlg_131(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=31)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=31)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/131.html', context)
	else:
		return render(request,'HackuizCTF/131.html',{})

@login_required(login_url="/list/login")
def chlg_132(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=32)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=32)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/132.html', context)
	else:
		return render(request,'HackuizCTF/132.html',{})

@login_required(login_url="/list/login")
def chlg_133(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=33)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=33)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/133.html', context)
	else:
		return render(request,'HackuizCTF/133.html',{})

@login_required(login_url="/list/login")
def chlg_134(request):
	if request.method=='POST':
		q=Challenges.objects.get(id=34)
		taker=Hackuiz_Taker.objects.get(user=request.user,challenge_name=34)
		if taker.completed==False:
			taker.attempts=taker.attempts + 1
			if taker.attempts <= 3:
				form=AnswerForm(request.POST)
				flag=request.POST['flag']
				crct_flag=q.challenge_solution
				if flag==crct_flag:
					messages.success(request, 'You have captured the flag successfully!!!')
					taker.completed=True
					taker.taker_score=taker.taker_score+q.challenge_score
				else:
					messages.success(request, 'Incorrect! Hack harder...!')
					taker.completed=False
				taker.save()
			else:
				messages.success(request, "Ohh!! As you have captured a wrong flag three times, This particular challenge is locked for you...")
		else:
			messages.success(request,"You have already captured the flag successfully")
		context={'taker':taker}
		return render(request, 'HackuizCTF/134.html', context)
	else:
		return render(request,'HackuizCTF/134.html',{})