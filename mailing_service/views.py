# from django.conf import settings
# from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render

from mailing_service.forms import ClientForm, MailingLogsForm, MailingMessageForm
from mailing_service.models import Client, Mailing, MailingLogs, MailingMessage
from blog.models import BlogMaterial
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from mailing_service.permissions import IsOwnerOrReadOnly
from mailing_service.services import _send_mail_email


# from mailing_service.services import get_cached_categories

def get_main_page(request):
    context = {
        'count_mailing_message': MailingMessage.objects.all().count(),
        'count_active_mailing_message': Mailing.objects.filter(status=True),
        'count_unique_clients': Client.objects.all().count(),
        'blog articles': BlogMaterial.objects.all()[:3]
    }
    return render(request, 'main_page.html', context=context)


class MailingMessageMailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = MailingMessage, Mailing
    permission_required = 'mailing_service.add_mailingmessage'
    success_url = reverse_lazy('mailing_service:list_mailingmessage')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        FormSet = inlineformset_factory(MailingMessage, Mailing, form=MailingMessageForm, extra=2)
        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        _send_mail_email(self.object.client, self.object.item, self.object.text)

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    # def get_queryset(self, *args, **kwargs):
    #     return Product.user.filter(is_verificated=True, is_activated=True)


class MailingMessageListView(ListView):
    model = MailingMessage
    success_url = reverse_lazy('mailing_service:list_mailingmessage')

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['category'] = get_cached_categories()
    #     return context_data

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(published=True)
    #     return queryset


class MailingMessageMailingDetailView(DetailView):
    model = MailingMessage, Mailing
    success_url = reverse_lazy('mailing_service:detail_mailingmessage')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        FormSet = inlineformset_factory(MailingMessage, Mailing, form=MailingMessageForm, extra=1)
        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.views_count += 1
    #     self.object.save()
    #     return self.object

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     if settings.CACHE_ENABLED:
    #         version_list = cache.get(f'version_list_{self.object.pk}')
    #         if version_list is None:
    #             version_list = self.object.version_set.all()
    #             cache.set(f'{self.object.pk}', version_list)
    #     else:
    #         version_list = self.object.version_set.all()
    #     context_data['versions'] = version_list
    #     return context_data


class MailingMessageMailingUpdateView(UpdateView):
    model = MailingMessage, Mailing
    form_class = MailingMessageForm
    # permission_required = 'mailing_service.change_mailingmessage'
    permission_classes = (IsOwnerOrReadOnly,)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        FormSet = inlineformset_factory(MailingMessage, Mailing, form=MailingMessageForm, extra=1)
        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class MailingMessageDeleteView(DeleteView):
    model = MailingMessage
    # permission_required = 'mailing_service.delete_mailingmessage'
    permission_classes = (IsOwnerOrReadOnly,)


class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    permission_required = 'mailing_service.add_client'
    success_url = reverse_lazy('mailing_service:list_clients')


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing_service:detail_client')
    # permission_required = 'mailing_service.view_client'
    permission_classes = (IsOwnerOrReadOnly,)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    # permission_required = 'mailing_service.change_client'
    permission_classes = (IsOwnerOrReadOnly,)


class ClientDeleteView(DeleteView):
    model = Client
    # permission_required = 'mailing_service.delete_client'
    success_url = reverse_lazy('mailing_service:list_clients')
    permission_classes = (IsOwnerOrReadOnly,)


class MailingLogsListView(ListView):
    model = MailingLogs
    permission_classes = (IsOwnerOrReadOnly,)


class MailingLogsDetailView(DetailView):
    model = MailingLogs
    form_class = MailingLogsForm
    success_url = reverse_lazy('mailing_service:detail')
    # permission_required = 'mailing_service.view_logs'
    permission_classes = (IsOwnerOrReadOnly,)

# def catalog_home(request):
#     product_list = Product.objects.all()
#     context = {
#         "object_list": product_list,
#
#     }
#     return render(request, 'mailingmessage_list.html', context)
#
#
# def catalog_contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         Contact.objects.create(name=name, tel=phone, message=message)
#     return render(request, 'contact_form.html')
#
#
# def catalog_product(request, pk):
#     # paginator = Paginator(product_list, 1)
#     # page_number = request.GET.get('page')
#     # page_obj = paginator.get_page(page_number)?  {'page_obj': page_obj}
#     context = {
#         "object_list": Product.objects.filter(pk=pk)
#     }
#     return render(request, 'mailingmessage_detail.html', context)
#
#
# def add_product(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         desc = request.POST.get('desc')
#         price = request.POST.get('price')
#         cat = request.POST.get('cat')
#         cat1, _ = Category.objects.get_or_create(name='Овощи', defaults={
#             "desc": "Описание категории овощи"
#         })
#         cat2, _ = Category.objects.get_or_create(name='Фрукты', defaults={
#             "desc": "Описание категории фрукты"
#         })
#         imd = request.POST.get('imd')
#         if str(cat) == str(cat1):
#             Product.objects.create(name=name, desc=desc, cat=cat1, price=price, imd=imd)
#         elif str(cat) == str(cat2):
#             Product.objects.create(name=name, desc=desc, cat=cat2, price=price, imd=imd)
#
#     return render(request, 'mailingmessage_form.html')
