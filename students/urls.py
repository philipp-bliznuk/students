from django.conf.urls import patterns, url

from .views import (
    StudentListView, StudentCreateView, StudentEditView, StudentDeleteView
)


urlpatterns = patterns(
    '',
    url(r'^$', StudentListView.as_view(), name='students_list'),
    url(r'^create/$', StudentCreateView.as_view(), name='student_create'),
    url(r'^(?P<student_id>\d+)/edit/$', StudentEditView.as_view(),
        name='student_edit'),
    url(r'^(?P<student_id>\d+)/delete/$', StudentDeleteView.as_view(),
        name='student_delete'),
)
