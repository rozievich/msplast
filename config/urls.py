from django.contrib import admin
from django.urls import path, include

from django.conf.urls import handler404

urlpatterns = [
    path('site/admin/', admin.site.urls),
    path('', include('main.urls'))
]
