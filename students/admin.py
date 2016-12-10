from django.contrib import admin

from core.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'birth_date', 'ticket_number')


admin.site.register(Student, StudentAdmin)
