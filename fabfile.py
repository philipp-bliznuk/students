import os, sys

from fabric.api import local, task
from fabric.colors import green, red


DEFAULT_MODE = 'dev'
SERVER_MODES = {
    'dev': 'dev',
}


def success(message):
    print(green(message))


def error(message):
    print(red(message))
    sys.exit()


def get_mode(mode):
    if mode not in SERVER_MODES:
        error('Mode "%s" - does not exist' % mode)
    return SERVER_MODES[mode]


def django_manage(command, mode):
    modename = get_mode(mode)
    return local('python manage.py %s --settings=settings.%s' % (command, modename))


@task
def smtp():
    success("Run SMTP server at localhost:1025")
    local("python -m smtpd -n -c DebuggingServer localhost:1025")


@task
def reset_db(mode=DEFAULT_MODE):
    proj_path = os.path.dirname(__file__)
    if proj_path not in sys.path:
        sys.path.append(proj_path)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.%s' % get_mode(mode))
    from django.conf import settings

    db_settings = settings.DATABASES['default']
    db_name = db_settings.get('NAME')
    db_path = os.path.join(settings.BASE_DIR, db_name)
    success('Remove database')
    try:
        os.remove(db_path)
    except:
        pass
    update_db(mode)


@task
def update_db(mode=DEFAULT_MODE):
    success('Sync DB')
    django_manage('syncdb --noinput', mode)


@task
def run(mode=DEFAULT_MODE):
    success('Run server')
    django_manage('runserver 0.0.0.0:8000', mode)


@task
def test(mode=DEFAULT_MODE):
    success('Run tests')
    django_manage('test', mode)


@task
def depending():
    success('Main requirements')
    local('pip install -r requirements.txt')
