from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .settings import DEBUG

urlpatterns = [
    path('site/admin/', admin.site.urls),
    path('', include('main.urls'))
]
if DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)\
                + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)