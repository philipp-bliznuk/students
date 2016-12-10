from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from .forms_mixin import AddCustomErrorMixin


INVALID_LOGIN_ERROR_KEY = 'invalid_login'
INACTIVE_ERROR_KEY = 'inactive'


class UserAuthenticationForm(AddCustomErrorMixin, AuthenticationForm):
    login = forms.CharField()
    password = forms.PasswordInput()

    error_messages = {
        INVALID_LOGIN_ERROR_KEY: "Login or password is incorrect.",
        INACTIVE_ERROR_KEY: "This account is inactive.",
    }

    def __init__(self, request=None, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        del self.fields['username']
        self.fields.keyOrder = ['login', 'password']

        for field_name, field in self.fields.iteritems():
            field.widget.attrs['class'] = 'form-control'

    def clean(self):
        login = self.cleaned_data.get('login')
        password = self.cleaned_data.get('password')

        if login and password:
            self.user_cache = authenticate(username=login, password=password)
            if self.user_cache is None:
                self.add_custom_error(INVALID_LOGIN_ERROR_KEY)
            elif not self.user_cache.is_active:
                self.add_custom_error(INACTIVE_ERROR_KEY)

        return self.cleaned_data
