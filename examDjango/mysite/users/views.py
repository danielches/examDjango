from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginUserForm, RegisterUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'loginpage.html'
    extra_context = {'title': 'Авторизация'}
    success_url = reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registerpage.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('users:login')