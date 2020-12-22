from django.conf.urls import url

from . import views
from .views import index

urlpatterns = [
    url('home', index, name='index'),
    url('(?P<variable_a>(\d+))/product', views.product, name='product'),


]