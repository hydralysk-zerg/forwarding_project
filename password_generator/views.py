from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'password_generator/index.html')


def password(request):

    characters = list('qwertyuiopasdfghjklzxcvbnm')
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()<>?'))
    if request.GET.get('number'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))
    thepassword = ''
    for letter in range(length):
        thepassword += random.choice(characters)

    return render(request, 'password_generator/password.html', {'password': thepassword})
