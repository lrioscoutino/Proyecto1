from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    list_users = ['Pedro', 'Luis', 'Manuel']
    context = {
        "user": "Mario",
        "age": 23,
        'users': list_users
    }
    return render(request, 'base.html', context=context)
