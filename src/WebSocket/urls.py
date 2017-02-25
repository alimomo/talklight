
"""
    - django-rest-framework has it's own URL routing extension for handling ViewSets where each
        ViewSet is registered with the router for a given URL prefix.
"""
from rest_framework.routers import DefaultRouter

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.current_base, name='base'),
]
