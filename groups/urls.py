from django.conf.urls import patterns, url

from .views import (
    GroupListView, GroupStudentsListView, GroupCreateView, GroupEditView,
    GroupDeleteView
)


urlpatterns = patterns(
    '',
    url(r'^$', GroupListView.as_view(), name='groups_list'),
    url(r'^create/$', GroupCreateView.as_view(), name='group_create'),
    url(r'^(?P<group_id>\d+)/students/$', GroupStudentsListView.as_view(),
        name='group_students'),
    url(r'^(?P<group_id>\d+)/edit/$', GroupEditView.as_view(),
        name='group_edit'),
    url(r'^(?P<group_id>\d+)/delete/$', GroupDeleteView.as_view(),
        name='group_delete'),
)
