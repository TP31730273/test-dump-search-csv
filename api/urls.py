
from django.urls import path
from .views import DataReaderView
urlpatterns = [
    path('dump_csv', DataReaderView.as_view(), name='dump_csv'),
    path('read_csv', DataReaderView.as_view(), name='read_csv'),
]