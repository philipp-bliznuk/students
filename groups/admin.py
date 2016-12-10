from django.contrib import admin

from core.models import Group, Student


class StudentsInline(admin.StackedInline):
    model = Student
    extra = 0


class GroupAdmin(admin.ModelAdmin):
    inlines = (StudentsInline,)
    list_display = ('name', 'warden', 'students_count')


admin.site.register(Group, GroupAdmin)
