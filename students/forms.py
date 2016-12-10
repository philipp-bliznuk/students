from django import forms

from core.models import Student
from core.forms_mixin import BootstrapForm


class StudentForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = Student
