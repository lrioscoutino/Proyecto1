import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from users.models import Students
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    View,
    CreateView,
)


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


class Home(View):

    def get(self, request):
        students = Students.objects.all()
        return render(request, 'home.html', {'students': students})


class AddStudent(View):

    def get(self, request):
        return render(request, "users/form_add.html")

    def post(self, request):
        body = {}
        if not request.POST:
            body = json.loads(request.body.decode('utf-8'))

        student = Students()
        student.name = request.POST.get('name',
                                        body.get('name'))
        student.address = request.POST.get('address',
                                           body.get('address'))
        student.birth_date = request.POST.get('birth_date',
                                              body.get('birth_date'))
        student.status = True
        student.save()
        return HttpResponseRedirect(reverse_lazy('home_view'))
    
    def get_success_url(self, request):
        return render(request, 'home.html')

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


class EditStudent(View):
    def get(self, request, student_id):
        student = Students.objects.get(id=student_id)
        return render(request, "users/form_add.html", {'student': student})

    def post(self, request, student_id):
        student = Students.objects.get(id=student_id)
        student.name = request.POST.get('name')
        student.address = request.POST.get('address')
        student.birth_date = request.POST.get('birth_date')
        student.status = True
        student.save()
        return HttpResponseRedirect(reverse_lazy('home_view'))


def edit_student(request, student_id):
    student = Students.objects.get(id=student_id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.address = request.POST.get('address')
        student.birth_date = request.POST.get('birth_date')
        student.status = True
        student.save()
        return HttpResponseRedirect(reverse_lazy('home_view'))
    else:
        return render(request, "users/form_add.html", {'student': student})


def delete_student(request, student_id):
    student = Students.objects.get(id=student_id)
    student.delete()
    return HttpResponseRedirect(reverse_lazy('home_view'))

