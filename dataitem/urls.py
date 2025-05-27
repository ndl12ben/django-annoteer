from django.urls import path
from .views import DataitemListView, DataitemCreateView

urlpatterns = [
    path('', DataitemListView.as_view(), name='dataitem_list'),
    path('new/', DataitemCreateView.as_view(), name='dataitem_create'),
]