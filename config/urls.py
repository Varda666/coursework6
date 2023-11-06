from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mailing_service.urls', namespace='mailing_service')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('users/', include(('users.urls', 'users'), namespace='users'))
    ]

