# Create your views here.
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ProductForm
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request) :
    books = Item.objects.filter(user=request.user)
    count = books.count()

    context = {
        'name': 'Sabrina Atha Shania',
        'account_name': request.user.username,
        'class': 'PBP-A',
        'NPM': '2206829591',
        'application_name': 'Galaxy Library',
        'count': count,
        'books': books,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_books(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_books.html", context)

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    
    if request.method == 'POST':
        if request.user == item.user:
            item.delete()
            return redirect('main:show_main') 
    return render(request, 'delete_item.html', {'item': item})

def add_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    
    if request.user == item.user:
        item.amount += 1
        item.save()
        return redirect('main:show_main') 

def subtract_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    
    if request.user == item.user:
        item.amount -= 1
        item.save()
        return redirect('main:show_main') 

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")