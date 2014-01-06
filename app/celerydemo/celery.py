from __future__ import absolute_import

import os

from celery import Celery

from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celerydemo.settings")

app = Celery("celerydemo")
app.conf.update(
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
)
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print ("Request: {0!r}".format(self.request))

if __name__ == "__main__":
    app.start()
