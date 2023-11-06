from django.urls import path
from django.contrib import admin
from django.views.decorators.cache import cache_page

from mailing_service.views import (MailingMessageListView, MailingMessageDeleteView, ClientCreateView, ClientUpdateView,
                                   ClientDetailView, ClientListView, ClientDeleteView, get_main_page,
                                   MailingLogsListView, MailingLogsDetailView, MailingMessageMailingCreateView,
                                   MailingMessageMailingUpdateView, MailingMessageMailingDetailView)

from config import settings
from django.conf.urls.static import static

app_name = 'mailing_service'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_main_page, name='main_page'),
    path('create/', MailingMessageMailingCreateView.as_view(), name='create_mailingmessage'),
    path('list/', cache_page(60)(MailingMessageListView.as_view()), name='list_mailingmessage'),
    path('detail/<int:pk>/', MailingMessageMailingDetailView.as_view(), name='detail_mailingmessage'),
    path('update/<int:pk>/', MailingMessageMailingUpdateView.as_view(), name='update_mailingmessage'),
    path('delete/<int:pk>/', MailingMessageDeleteView.as_view(), name='delete_mailingmessage'),
    path('create/client/', ClientCreateView.as_view(), name='create_client'),
    path('clients/', cache_page(60)(ClientListView.as_view()), name='list_clients'),
    path('detail/client/<int:pk>/', ClientDetailView.as_view(), name='detail_client'),
    path('update/client/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('delete/client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('logs/', MailingLogsListView.as_view(), name='delete_client'),
    path('detail/logs/<int:pk>/', MailingLogsDetailView.as_view(), name='delete_client'),

    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)