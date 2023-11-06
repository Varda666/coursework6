from django import forms
from django.views.generic import CreateView

from mailing_service.models import Client, MailingMessage, Mailing, MailingLogs


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        exclude = ('user',)


    # def clean_first_name(self):
    #     cleaned_data = self.cleaned_data.get('name', 'desc')
    #     list_forbidden_product = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    #     for item in list_forbidden_product:
    #         if item in cleaned_data:
    #             raise forms.ValidationError('Ошибка, связанная с использованием запрещенных слов')
    #         return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = 'form-control'


class MailingMessageForm(forms.ModelForm):

    class Meta:
        model = MailingMessage
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = 'form-control'


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mailing
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = 'form-control'


class MailingLogsForm(forms.ModelForm):

    class Meta:
        model = MailingLogs
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = 'form-control'
