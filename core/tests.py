from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.test import TestCase, Client

from .models import Student, Group


class CreateStudentAndGroupTestCase(TestCase):
    USER_NAME = 'testuser'
    USER_EMAIL = 'user@test.com'
    USER_PASSWORD = 'secret'
    STUDENT_NAME = 'Test Student'
    GROUP_NAME = 'Test Group'

    def setUp(self):
        self.client = Client()
        User.objects.create_superuser(
            username=self.USER_NAME,
            email=self.USER_EMAIL,
            password=self.USER_PASSWORD
        )

    def login(self):
        return self.client.login(
            username=self.USER_NAME, password=self.USER_PASSWORD
        )

    def test_login(self):
        self.assertTrue(self.login())

    def test_add_student_and_group(self):
        self.login()
        student_data = {
            'name': self.STUDENT_NAME,
            'birth_date': '1992-09-30',
            'ticket_number': '666',
        }
        self.client.post(reverse_lazy('students:student_create'), student_data)
        student = Student.objects.filter(name=self.STUDENT_NAME).first()
        self.assertTrue(student is not None)

        group_data = {
            'name': self.GROUP_NAME,
            'warden': student.id
        }
        self.client.post(reverse_lazy('groups:group_create'), group_data)
        self.assertTrue(Group.objects.filter(name=self.GROUP_NAME).exists())

    def tearDown(self):
        del self.client
