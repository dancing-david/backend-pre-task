from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('contacts', views.ContactsAPIView.as_view(), name='contacts'),
    path('contact/<int:contact_id>', views.ContactAPIView.as_view(), name='contact'),
]
