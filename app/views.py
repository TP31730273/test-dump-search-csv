from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.http import JsonResponse


class DataTable(View):

    def get(self, request):
        return render(
            request=request,
            context={"table_head_list": settings.VALID_CSV_KEYS},
            template_name="data_table.html",
        )


class DataTableColumnsView(View):
    def get(self, request):
        return JsonResponse(data={"table_columns": settings.VALID_CSV_KEYS})
