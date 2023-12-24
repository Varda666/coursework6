from django.conf import settings
# from django.core.cache import cache
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

# from mailing_service.models import Category
from django.core.mail import send_mail

from mailing_service.models import Mailing


# def get_cached_categories():
#     if settings.CACHE_ENABLED:
#         category_list = cache.get('category')
#         if category_list is None:
#             category_list = Category.objects.all()
#             cache.set('category', category_list)
#             return category_list
#         else:
#             return category_list


def _send_mail_email(recipient_list, subject, message):
    def job():
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient_list]
        )
    scheduler = BlockingScheduler()
    if Mailing.datetime_from < datetime.now() < Mailing.datetime_to:
        scheduler.add_job(job, 'interval', days=Mailing.frequency)
        scheduler.start()
