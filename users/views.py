from django.shortcuts import render
from django.http import HttpResponse
from users.models import Students


# Create your views here.
def home_view(request):
    list_users = ['Pedro', 'Luis', 'Manuel']
    context = {
        "user": "Mario",
        "age": 23,
        'users': list_users
    }
    return render(request, 'base.html', context=context)


def home(request):
    students = Students.objects.all()
    return render(request, 'home.html', {'students':students})


def about(request):
    return render(request, 'about.html')