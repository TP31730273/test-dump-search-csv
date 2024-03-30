from django.urls import path
from .views import DataTable, DataTableColumnsView

urlpatterns = [
    path("data_table", DataTable.as_view(), name="data_table"),
    path("data_columns", DataTableColumnsView.as_view(), name="data_table"),
]
