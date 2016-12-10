from django.core.management.base import BaseCommand

from core.models import Group


class Command(BaseCommand):
    def handle(self, *args, **options):
        for group in Group.objects.select_related('students'):
            self.stdout.write(group.name)
            for student_name in group.students.values_list('name', flat=True):
                self.stdout.write('{:->30}'.format(student_name))
