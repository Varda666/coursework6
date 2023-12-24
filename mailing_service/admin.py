from django.contrib import admin

from mailing_service.models import Client, MailingMessage, Mailing


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'comment', 'user')
    list_filter = ('email', 'first_name', 'last_name', 'comment', 'user')
    search_fields = ('email', 'first_name', 'last_name', 'comment', 'user')


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ('item', 'text', 'clients', 'user')
    list_filter = ('item', 'text', 'user')
    search_fields = ('item', 'text', 'user')

    def clients(self, obj):
        return ", ".join([c.email for c in obj.clients.all()])
    clients.short_description = "Clients"


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('message', 'datetime_from', 'datetime_to', 'frequency', 'status')
    list_filter = ('message', 'datetime_from', 'datetime_to', 'frequency', 'status')
    search_fields = ('message', 'datetime_from', 'datetime_to', 'frequency', 'status')
