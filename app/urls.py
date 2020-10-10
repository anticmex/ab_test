from django.urls import path, register_converter
from . import views

from app.views import landing, stats, index, alternate
from .converters import TextParcer

register_converter(TextParcer, '<from_landing>')
urlpatterns = [
    path('', index, name='index'),
    path('landing/', landing, name='landing'),
    path('landing_alternate/', alternate, name='alternate'),
    path('stats/', stats, name='stats'),
]
