from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name='home'),
    path('new_search', new_search, name='new_search')

]