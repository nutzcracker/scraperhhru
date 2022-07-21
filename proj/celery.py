import os
from celery.schedules import crontab
from celery import Celery


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')



# https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html
app.conf.beat_schedule = {
        # Название задачи
    'my-super-sum-every-5-min' : {
                # Регистрируем задачу. Для этого в качестве значения ключа task
                # Указываем полный путь до созданного нами ранее таска(функции)
        'task': 'demoapp.tasks.add',
                 # Периодичность с которой мы будем запускать нашу задачу
                 # minute='*/5' - говорит о том, что задача должна выполнятся каждые 1 мин.
        'schedule': crontab(minute='*/1'),
                # Аргументы которые будет принимать функция
                'args': (5, 8),
    }
}