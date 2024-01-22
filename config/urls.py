from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .settings import DEBUG

urlpatterns = [
                  path('site/admin/', admin.site.urls),

              ] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('main.urls'))

)
if DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) \
                   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
