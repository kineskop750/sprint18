from django.shortcuts import render,redirect
from .models import CustomUser
from .forms import CustomUserForm

from django.http import HttpResponseRedirect

def index(request):
	return render(request,'index.html')

def get_all_users(request):
	users = CustomUser.objects.order_by('id')
	context = {'users':users}
	return render(request,'user/all_user.html',context)

def new_user(request):
	if request.method != "POST":
		form = CustomUserForm()
	else:
		form = CustomUserForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('get_all_users')
	return render(request,'user/new_user.html',{'form':form})

def get_by_id(request,id):
	full = CustomUser.get_by_id(id)
	return render(request,'user/user.html',{'full':full})

def edit_user(request,edit_id):
	user = CustomUser.objects.get(pk=edit_id)
	if request.method != 'POST':
		form = CustomUserForm()
	else:
		form = CustomUserForm(instance=user,data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('get_all_users')
	return render(request,'user/edit_user.html',{'user':user,'form':form})

def user_delete(request,delete_id):
	CustomUser.delete_by_id(delete_id)
	return redirect('get_all_users')
