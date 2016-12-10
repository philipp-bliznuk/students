from django import forms

from core.models import Group
from core.forms_mixin import BootstrapForm


class GroupForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = Group
