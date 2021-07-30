from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html', {'password':'njdbcibcicfb'})

def about(request):
    return render(request, 'generator/about.html')
    
def password(request):

        thepassword = ''

        characters = list('abcdefghijklmnopqrtsuvwxyz')

        if request.GET.get('Uppercase'):
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

        if request.GET.get('uppercase'):
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

        if request.GET.get('Special Characters'):
            characters.extend(list('!@#$%^&*'))

        if request.GET.get('numbers'):
            characters.extend(list('1234567890'))


        length = int(request.GET.get('length', 12))

        for x in range(length):
            thepassword += random.choice(characters)



        return render(request, 'generator/password.html', {'password': thepassword})
