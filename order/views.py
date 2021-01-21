from django.shortcuts import render,redirect
from .models import Order
from author.models import Author
from book.models import Book
from .forms import OrderForm

# Create your views here.

def get_all_orders(request):
	orders = Order.objects.all()
	context = {'orders':orders}

	return render(request,'order/all_order.html',context)

def get_order(request,id):
	full = Order.get_by_id(id)
	return render(request,'order/order.html',{'full':full})

def new_order(request):
	if request.method != "POST":
		form = OrderForm()
	else:
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('get_all_orders')
	return render(request,'order/new_order.html',{'form':form})

def delete_order(request,id):
	Order.delete_by_id(id)
	return redirect('get_all_orders')

def edit_order(request,id):
	order = Order.objects.get(pk=id)
	if request.method != 'POST':
		form = OrderForm()
	else:
		form = OrderForm(instance=order,data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('get_all_orders')
	return render(request,'order/edit_order.html',{'order':order,'form':form})