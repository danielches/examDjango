from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from books.models import *
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm
from books.forms import SearchForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'loginpage.html'
    extra_context = {'title': 'Авторизация', 'searchform': SearchForm()}
    success_url = reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registerpage.html'
    extra_context = {'title': "Регистрация", 'genreslist': Genre.objects.all(), 'searchform': SearchForm()}
    success_url = reverse_lazy('users:login')


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'profile.html'
    extra_context = {
        'title': "Профиль пользователя",
        'genreslist': Genre.objects.all(),
        'searchform': SearchForm()
    }

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("home")
    template_name = "password_change_form.html"
    extra_context = {
        'genreslist': Genre.objects.all(), 'searchform': SearchForm()
    }
