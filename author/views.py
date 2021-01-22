from django.shortcuts import render, redirect
from .models import Author
from .forms import AuthorForm
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer


def get_all_authors(request):
	authors = Author.objects.order_by('id')
	context = {'authors': authors}
	return render(request, 'author/all_authors.html', context)


def get_author(request,id):
	full = Author.get_by_id(id)
	return render(request, 'author/author.html', {'full': full})


def delete_author(request, id):
	Author.delete_by_id(id)
	return redirect('get_all_authors')


def author_form(request, id=0):
	if request.method == 'GET':
		if id == 0:
			form = AuthorForm()
		else:
			author = Author.get_by_id(id)
			form = AuthorForm(instance=author)
		return render(request, 'author/author_form.html', {'form': form})
	else:
		if id == 0:
			form = AuthorForm(request.POST)
		else:
			author = Author.get_by_id(id)
			form = AuthorForm(request.POST, instance=author)
		if form.is_valid():
			form.save()
		return redirect('get_all_authors')

class AuthorView(ModelViewSet):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer
