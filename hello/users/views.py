from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import Contact  
from .forms import ProductForm
from django.http import HttpResponse


def home(request):
	return render(request,'users/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
 
@login_required
def test(request):
	return render(request,'users/test.html')


def contact(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            print(email)
            return redirect('home')
   
    else:
        form = Contact()

    return render(request,'users/contact.html',{'form':form})
def product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {

    'form':form
    }
    return render(request,'users/product.html',context)
