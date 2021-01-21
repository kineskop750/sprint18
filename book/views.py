from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def get_all_books(request):
	books = Book.objects.all()
	context = {'books':books}
	return render(request,'book/all_books.html',context)

def get_book(request,id):
	full = Book.get_by_id(id)
	return render(request,'book/{id}.html',{'full':full})

def new_book(request):
	if request.method != "POST":
		form = BookForm()
	else:
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('get_all_books')
	return render(request,'book/new_book.html',{'form':form})

def delete_book(request, id):
	Book.objects.delete_by_id(id)
	return redirect('get_all_books')

def edit_book(request,id):
	book = Book.objects.get(pk=id)
	if request.method != 'POST':
		form = BookForm()
	else:
		form = BookForm(instance=book,data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('get_all_books')
	return render(request,'book/edit_book.html',{'book':book,'form':form})
	