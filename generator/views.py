from django.shortcuts import render
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')
    

def about(request):
    return render(request, 'generator/about.html')


def password(request):
    characters = []
    for i in range(97,123):
        characters.append(chr(i))
    
    if request.GET.get('uppercase'):
        for i in range(65,91):
            characters.extend(chr(i))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()-+=_[]'))

    if request.GET.get('numbers'):
        for i in range(48,58):
            characters.extend(chr(i))

    length = int(request.GET.get('length'))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})





