from django.shortcuts import render
from random import choice

def home_page(request):
    return render(request, 'home_page.html')

def password(request):
    length = int(request.GET.get('length'))
    words = list('qazwsxedcrfvtgbyhnujmikolp')
    thepass = ''

    if request.GET.get('uppercase'):
        words.extend(list('QAZWSXEDCRFVTGBYHNUJMIKOLP'))
    if request.GET.get('numbers'):
        words.extend(list('0123456789'))
    if request.GET.get('special'):
        words.extend(list('!@#$%^&*()'))

    for word in range(length):
        thepass += choice(words)

    return render(request, 'password.html', {'password': thepass})