from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from users.models import User
from django import forms


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.ChoiceField):
                field.widget.attrs['class'] = 'form-select'
            elif isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class StylePasswordResetMixin:
    """
   Обновление стилей форм восстановления пароля
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control mt-2',
                'autocomplete': 'off'
            })

class UserLoginForm(StyleFormMixin, AuthenticationForm):
    """
    Форма авторизации на сайте
    """
    pass
class UserRegisterForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class UserForgotPasswordForm(StylePasswordResetMixin, PasswordResetForm):
    """
    Запрос на восстановление пароля
    """
    pass

class UserSetNewPasswordForm(StylePasswordResetMixin, SetPasswordForm):
    """
    Изменение пароля пользователя после подтверждения
    """
    pass

class UserProfileForm(StyleFormMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'avatar', 'country')

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()

