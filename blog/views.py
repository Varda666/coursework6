from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
# from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import BlogMaterial
from blog.permissions import IsOwnerOrReadOnly
from config import settings


class BlogMaterialCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = BlogMaterial
    fields = ('name', 'slug', 'imd')
    permission_required = 'blog.add_blogmaterial'
    success_url = reverse_lazy('blog:list')


class BlogMaterialListView(ListView):
    model = BlogMaterial

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(published=True)
    #     return queryset


class BlogMaterialDetailView(DetailView):
    model = BlogMaterial
    fields = '__all__'
    success_url = reverse_lazy('blog:detail')
    permission_classes = (IsOwnerOrReadOnly,)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

    def send_mess_email(self, queryset):
        self.object = super().get_object(queryset)
        if self.object.views_count > 10:
            send_mail(
                subject='Поздравление',
                message='Поздравляем, у вас 10 просмотров',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.object.email]
            )


class BlogMaterialUpdateView(UpdateView):
    model = BlogMaterial
    fields = '__all__'
    # permission_required = 'blog.change_blogmaterial'
    permission_classes = (IsOwnerOrReadOnly,)
    # success_url = reverse_lazy('blog:list')

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogMaterialDeleteView(DeleteView):
    model = BlogMaterial
    # permission_required = 'blog.delete_blogmaterial'
    permission_classes = (IsOwnerOrReadOnly,)
    success_url = reverse_lazy('blog:list')
