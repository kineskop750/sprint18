from django.shortcuts import render, redirect
from .models import Author
from .forms import AuthorForm

# Create your views here.
def get_all_authors(request):
	authors = Author.objects.order_by('id')
	context = {'authors':authors}
	return render(request, 'author/all_authors.html',context)

def get_author(request,id):
	full = Author.get_by_id(id)
	return render(request,'author/{id}.html',{'full':full})

def new_author(request):
	if request.method != "POST":
		form = AuthorForm()
	else:
		form = AuthorForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('get_all_authors')
	return render(request,'author/new_author.html',{'form':form})

def delete_author(request, id):
	Author.objects.delete_by_id(id)
	return redirect('get_all_authors')

def edit_author(request,id):
	author = Author.objects.get(pk=id)
	if request.method != 'POST':
		form = AuthorForm()
	else:
		form = AuthorForm(instance=author,data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('get_all_authors')
	return render(request,'author/edit_author.html',{'author':author,'form':form})