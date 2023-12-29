import random

from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from users.models import User
from users.forms import UserRegisterForm, UserProfileForm
from django.urls import reverse_lazy,reverse
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect



class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_engine = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Поздравляем с регистрацией',
            message='Вы зарегистрировались на нашей платформе',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)

class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user



def generate_new_password(request):
    new_password = ''.join([str(random.randint(1, 9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()

    return redirect(reverse('catalog:index'))