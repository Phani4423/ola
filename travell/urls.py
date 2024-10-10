from django.urls import path
from travell.views import *
app_name = 'travell'

urlpatterns = [
    path('hydrabed/',hydrabed,name='hydrabed'),
]