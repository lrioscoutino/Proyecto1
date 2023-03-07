from django.urls import path, include
from users.views import (
    Home,
    AddStudent,
    home,
    about,
    add_student,
    edit_student,
    delete_student,
    EditStudent,
)
from django.contrib.auth.views import LoginView, LogoutView
from users.routers import router

urlpatterns = [
    path('home2/', home, name='home2_view'),
    path('home/', Home.as_view(), name='home_view'),
    path('add-student/', AddStudent.as_view(), name='add_student_view'),
    path('edit-student/<int:student_id>/', EditStudent.as_view(), name='edit_student_view'),
    path('delete-student/<int:student_id>/', delete_student, name='delete_student_view'),
    path('about/', about, name='about_view'),
    path('', LoginView.as_view(template_name='base.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/v1/', include(router.urls))

]
