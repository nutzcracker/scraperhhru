from django.contrib import admin
from django.urls import path
from django.urls import path
from .views import MainView, filter_view
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('filter', filter_view, name='filter'),

]
