from django.shortcuts import render
from django.http import HttpResponse
from users.models import Students
from django.urls import reverse_lazy


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
    return render(request, 'home.html', {'students': students})


def about(request):
    return render(request, 'about.html')


def add_student(request):
    if request.method == 'POST':
        student = Students()
        student.name = request.POST.get('name')
        student.address = request.POST.get('address')
        student.birth_date = request.POST.get('birth_date')
        student.status = True
        student.save()
        return reverse_lazy('home_view')
    else:
        return render(request, "users/form_add.html")


def edit_student(request, student_id):
    student = Students.objects.get(id=student_id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.address = request.POST.get('address')
        student.birth_date = request.POST.get('birth_date')
        student.status = True
        student.save()

    else:
        return render(request, "users/form_add.html", {'student': student})
