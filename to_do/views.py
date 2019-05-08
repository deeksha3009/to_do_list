from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from to_do.models import Task
from django.template import RequestContext

def home(request):
	if request.user.is_authenticated:
		return redirect("/dashboard/")

	return render(request,"home.html")

def signin(request):
	if request.method=="POST":
		username = request.POST['username']
		print(username)
		password = request.POST['password']
		print(password)
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			login(request,user)
			return redirect("/dashboard/")
		else:
			return HttpResponse("please Check if the username and password is correct")

	return render(request,"signin.html")
	

def signup(request):
	if request.method == "POST":
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		email = request.POST.get("email")
		print(email)
		user = authenticate(username=username, password=password)
		if user is None:
			user = User.objects.create_user(username, email, password)
			login(request,user)
			return redirect("/dashboard/")
		else:
			return HttpResponse("Please Check the Info, User might already exist.")
	return render(request, "signup.html")


def signout(request):
	logout(request)
	return render(request,"home.html")

def Dashboard(request):
	user=request.user
	no_tasks = Task.objects.filter(user=user)
	return render(request,"1.html" ,{"tasks":no_tasks})

def add_task(request):
	user = request.user
	if request.method == "POST":
		title=request.POST.get('title')
		context=request.POST.get('description')
		date=request.POST.get('due_date')
		post = Task(title=title,description=context,last_date=date,user=user)
		post.save()
		return redirect("/dashboard/")

	return render(request, "1.html") 

def view_task(request,tid):
	specific = Task.objects.get(pk=tid)
	return render(request, "task.html", {"one_task":specific})

def complete(request,tid):
	user = request.user
	try:
		task=Task.objects.get(pk=tid,user=user)
		if task.complete:
			task.complete = 0
		else:
			task.complete = 1
		task.save()
		task.delete()
		return render(request,"done.html")
	except Exception:
		return HttpResponse("Sorry You are not allowed to access This task ")

def delete(request,tid):
	User=request.user
	Task.objects.filter(pk=tid,user=User).delete()
	return render(request,"delete.html")
