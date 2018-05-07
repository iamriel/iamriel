from django.urls import path
from django.contrib import admin

from main import views
from accounts.views import (
    ContactFormView,
)


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('pasmo/', admin.site.urls),
]
