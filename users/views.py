import random

from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

# from config import settings
from users.forms import UserForm, UserRegisterForm
from users.models import User
from users.services import _send_mail_email, _send_mail_password


class LoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('users:profile')


class LogoutView(LogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('mailing_service:main_page')
    template_name = 'users/register.html'

    def form_valid(self, form):
        self.object = form.save()
        _send_mail_email(self.object.pk, self.object.email)
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9) for _ in range(6))])
    request.user.set_password(new_password)
    request.user.save()
    _send_mail_password(new_password, request.user.email)
    return redirect(reverse('users:profile'))


def verificate_user(request):
    pk = request['pk']
    user = User.objects.get(pk=pk)
    user.is_verificated = True
    user.is_active = True
