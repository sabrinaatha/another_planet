# Create your views here.
from django.shortcuts import render, redirect
from .models import Item
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

def show_main(request) :
    books = Item.objects.all()
    context = {
        'name': 'Sabrina Atha Shania',
        'class': 'PBP-A',
        'NPM': '2206829591',
        'application_name': 'Galaxy Library',
        'books': books,
    }
    Item.objects.get_or_create(name='Harry Potter and the Philosopher\'s Stone', amount=10, description= 'The first book in the Harry Potter series was entitled Harry Potter and the Philosopher\'s Stone. This series opening novel is the part that introduces every important character in the Harry Potter story. The story in this first novel comes from the story of Harry Potter, who for 11 years has lived a miserable life with his cousin\'s family.')
    Item.objects.get_or_create(name='Harry Potter and the Chamber of Secrets', amount=35, description= 'The second book in the Harry Potter series is entitled Harry Potter and the Chamber of Secrets. This second book tells the story of Harry Potter and his friends when their school was in an uproar because of a mysterious terror. Harry and his friends then have to face threats from monsters that are in the Chamber of Secrets at Hogwarts.')
    Item.objects.get_or_create(name='Harry Potter and the Prisoner of Azkaban', amount=28, description='The story of the adventures of Harry Potter and his friends continues in the third book in the series, namely Harry Potter and the Prisoner of Azkaban. This third book in the series tells the story of Harry Potter and his friends who have to face threats from mysterious prisoners who have escaped from Azkaban, the most stringent wizard prison in the wizarding world.')
 
    return render(request, "main.html", context)

def create_books(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_books.html", context)

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