from django.urls import path
from contact.views import ListView, DetailView


urlpatterns = [
    path('<int:id>/', DetailView.as_view(), name='details'),
    path('', ListView.as_view(), name='list'),
]
