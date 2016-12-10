from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.models import Group, Student
from .forms import GroupForm


class GroupListView(LoginRequiredMixin, ListView):
    template_name = 'groups_list.html'
    paginate_by = 20
    context_object_name = 'groups'
    model = Group


class GroupStudentsListView(LoginRequiredMixin, ListView):
    template_name = 'group_students_list.html'
    paginate_by = 20
    context_object_name = 'students'
    pk_url_kwarg = 'group_id'
    model = Student

    def get_context_data(self, **kwargs):
        context = super(GroupStudentsListView, self).get_context_data(**kwargs)
        context['group_name'] = self.get_group()
        return context

    def get_queryset(self):
        return Student.objects.filter(group=self.get_group())

    def get_group(self):
        return Group.objects.filter(
            pk=self.kwargs.get(self.pk_url_kwarg)
        ).first()


class GroupCreateView(LoginRequiredMixin, CreateView):
    template_name = 'group_create.html'
    success_url = reverse_lazy('groups:groups_list')
    form_class = GroupForm
    model = Group

    def form_valid(self, form):
        self.object = form.save()
        self.object.warden.group = self.object
        self.object.warden.save()
        return super(GroupCreateView, self).form_valid(form)


class GroupEditView(LoginRequiredMixin, UpdateView):
    template_name = 'group_edit.html'
    success_url = reverse_lazy('groups:groups_list')
    pk_url_kwarg = 'group_id'
    form_class = GroupForm
    model = Group


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('groups:groups_list')
    pk_url_kwarg = 'group_id'
    model = Group
