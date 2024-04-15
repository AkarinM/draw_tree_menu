
from django.urls import path

from menu.views import draw_view

urlpatterns = [
    path('view/', draw_view, name='draw_view'),
]
