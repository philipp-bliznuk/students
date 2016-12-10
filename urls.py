from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from yawdadmin import admin_site

from core.views import UserAuthenticationView, IndexView


admin.autodiscover()
admin_site._registry.update(admin.site._registry)


urlpatterns = patterns('',
    url(r'^login/$', UserAuthenticationView.as_view(), name='auth_login'),
    url(r'^logout/$', auth_views.logout,
        {'next_page': reverse_lazy(settings.LOGOUT_REDIRECT_URL)},
        name='auth_logout'),

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^groups/', include('groups.urls', namespace='groups')),
    url(r'^admin/', include(admin_site.urls)),
)
