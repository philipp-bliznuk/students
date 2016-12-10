from django.db import models
from django.db.models.signals import post_save, post_delete


class Student(models.Model):
    group = models.ForeignKey(
        'Group', related_name='students', null=True, blank=True
    )
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    ticket_number = models.IntegerField()

    def __unicode__(self):
        return self.name


class Group(models.Model):
    warden = models.ForeignKey(Student, related_name='groups', unique=True)
    name = models.CharField(max_length=10)

    @property
    def students_count(self):
        return self.students.count()

    def __unicode__(self):
        return self.name


class LogHistory(models.Model):
    CREATED, EDITED, DELETED = range(1, 4)
    ACTION_CHOICES = (
        (CREATED, 'Created'),
        (EDITED, 'Edited'),
        (DELETED, 'Deleted'),
    )

    action = models.PositiveSmallIntegerField(
        max_length=1, choices=ACTION_CHOICES
    )
    instance_info = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def action_display(self):
        return self.get_action_display()

    @staticmethod
    def get_instance_info(sender, instance):
        return '<{}> `{}`'.format(sender.__name__, instance.__unicode__())

    def __unicode__(self):
        return '''{self.action_display} {self.instance_info}
        at {self.created_at:%Y-%m-%d %H:%M:%S}'''.format(self=self)


MODELS_FOR_LOGGING = [Student, Group]


def handle_post_save(sender, instance, created, **kwargs):
    if not kwargs.get('raw'):
        action = LogHistory.CREATED if created else LogHistory.EDITED
        LogHistory.objects.create(
            instance_info=LogHistory.get_instance_info(sender, instance),
            action=action
        )


def handle_post_delete(sender, instance, **kwargs):
    if not kwargs.get('raw'):
        LogHistory.objects.create(
            instance_info=LogHistory.get_instance_info(sender, instance),
            action=LogHistory.DELETED
        )


for model in MODELS_FOR_LOGGING:
    post_save.connect(handle_post_save, model)
    post_delete.connect(handle_post_delete, model)
