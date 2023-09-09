from django.shortcuts import render, redirect
from .models import Books
from .forms import Forms


def show_main(request) :
    context = {
        'name': 'Sabrina Atha Shania',
        'class': 'PBP-A',
        'application_name': 'Book Collections of Galaxy Library',
    }
    book1 = Books.objects.get_or_create(name='Harry Potter and the Philosopher\'s Stone', amount=10, description= 'The first book in the Harry Potter series was entitled Harry Potter and the Philosopher\'s Stone. This series opening novel is the part that introduces every important character in the Harry Potter story. The story in this first novel comes from the story of Harry Potter, who for 11 years has lived a miserable life with his cousin\'s family.')
    Books.objects.get_or_create(name='Harry Potter and the Chamber of Secrets', amount=35, description= 'The second book in the Harry Potter series is entitled Harry Potter and the Chamber of Secrets. This second book tells the story of Harry Potter and his friends when their school was in an uproar because of a mysterious terror. Harry and his friends then have to face threats from monsters that are in the Chamber of Secrets at Hogwarts.')
    Books.objects.get_or_create(name='Harry Potter and the Prisoner of Azkaban', amount=28, description='The story of the adventures of Harry Potter and his friends continues in the third book in the series, namely Harry Potter and the Prisoner of Azkaban. This third book in the series tells the story of Harry Potter and his friends who have to face threats from mysterious prisoners who have escaped from Azkaban, the most stringent wizard prison in the wizarding world.')
    
    books = Books.objects.all()
    form = Forms(request.POST or None)

    if request.method == "POST" :
        if form.is_valid() :
            form.save()
            return redirect("/main")
 
    return render(request, "main.html", {'books': books, 'form': form, 'detail' : context})
# Create your views here.
