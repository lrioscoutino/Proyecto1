from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from users.models import Students



# Create your views here.
def home_view(request):
    list_users = ['Pedro', 'Luis', 'Manuel']
    context = {
        "user": "Mario",
        "age": 23,
        'students': list_users
    }
    return render(request, 'base.html', context=context)


def home(request):
    students = Students.objects.all()
    return render(request, 'home.html', {'students': students})


def add_student(request):
    print(request)
    if request.method == 'POST':
        student = Students()
        student.name = request.POST.get('name')
        student.address = request.POST.get('address')
        student.birth_date = request.POST.get('birth_date')
        student.status = True
        student.control_number = request.POST.get('control_number')
        student.save()
        return reverse_lazy('home_view')
    else:
        return render(request, "students/form_add.html")


def about(request):
    return render(request, 'about.html')
