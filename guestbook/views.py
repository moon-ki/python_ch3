from django.shortcuts import render
from guestbook.models import Guestbook
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'guestbook/index.html')

def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']#name은 html의 테그 name이다.
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')