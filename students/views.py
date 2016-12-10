from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.models import Student
from .forms import StudentForm


class StudentListView(LoginRequiredMixin, ListView):
    template_name = 'students_list.html'
    paginate_by = 20
    context_object_name = 'students'
    model = Student


class StudentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'student_create.html'
    success_url = reverse_lazy('students:students_list')
    form_class = StudentForm
    model = Student


class StudentEditView(LoginRequiredMixin, UpdateView):
    template_name = 'student_edit.html'
    success_url = reverse_lazy('students:students_list')
    pk_url_kwarg = 'student_id'
    form_class = StudentForm
    model = Student


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('students:students_list')
    pk_url_kwarg = 'student_id'
    model = Student
