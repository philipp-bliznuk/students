from django.conf import settings
from django.utils.http import is_safe_url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, RedirectView
from django.contrib.auth import login as auth_login

from .forms import UserAuthenticationForm


class UserAuthenticationView(FormView):
    form_class = UserAuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        if is_safe_url(url=self.request.POST.get('next'),
                       host=self.request.get_host()):
            return self.request.POST.get('next')
        return reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super(UserAuthenticationView, self).form_valid(form)


class IndexView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return reverse_lazy('students:students_list')
        return reverse_lazy('auth_login')
