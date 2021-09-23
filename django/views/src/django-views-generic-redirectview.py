from django.views.generic import RedirectView
from django.urls import path

urlpatterns = [
    path('/index.html', RedirectView.as_view(permanent=False, url='/main')),
]
