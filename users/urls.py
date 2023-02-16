from django.urls import path
from users.views import home, about
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home/', home, name='home_view'),
    path('about/', about, name='about_view'),
    path('', LoginView.as_view(template_name='base.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
