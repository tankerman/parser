from django.urls import path, include

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('list/', ListView.as_view(), name='list_view')
    
]
