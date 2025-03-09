"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('',views.index, name='index'),
    # Page that shows all topics.
    path('topics/',views.topics, name='topics'),
    # Detail page for single topics.
    path('topics/<int:topic_id>/',views.topics, name='topics'),
]