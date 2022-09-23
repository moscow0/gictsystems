from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import Index, Get, Post

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('items', Get.as_view(), name='get'),
    path('post', Post.as_view(), name='post')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)