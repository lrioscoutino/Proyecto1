from django.urls import path
from users.views import home, about, add_student, edit_student
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home/', home, name='home_view'),
    path('add-student/', add_student, name='add_student_view'),
    path('edit-student/<int:student_id>/', edit_student, name='edit_student_view'),
    path('about/', about, name='about_view'),
    path('', LoginView.as_view(template_name='base.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
