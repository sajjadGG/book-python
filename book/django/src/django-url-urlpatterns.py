from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]