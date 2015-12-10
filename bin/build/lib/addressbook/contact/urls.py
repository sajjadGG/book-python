from django.conf.urls import url
from contact.views import WizytowkaView


urlpatterns = [
    url(r'wizytowka/(?P<name>\w+)', WizytowkaView.as_view())
]