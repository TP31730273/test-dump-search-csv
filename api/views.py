from typing import Union
import pandas as pd
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import serializers
from .models import CallData
from django.db import transaction
from .exceptions import QueryParmNotValidException
from django.conf import settings

# Create your views here.


class DataReaderView(APIView):
    parser_classes = (
        MultiPartParser,
        FormParser,
    )

    class CsvDataSerializer(serializers.ModelSerializer):
        pass

    def query_param_validator(self, params: dict) -> Union[str, None]:
        if len(params) > 0:
            param = params[0]
            valid_query_params = list(settings.VALID_CSV_KEYS.values())
            if param == "_":
                return None
            if param not in valid_query_params:
                raise QueryParmNotValidException()

            return param
        else:
            return None

    def get(self, request, format=None):
        search_param = self.request.query_params
        search_key = self.query_param_validator(params=list(search_param.keys()))
        search_data_params = {}
        if search_key:
            search_data_params = {
                f"csv_data__{search_key}__icontains": search_param.get(search_key, "")
            }
        query_set = list(
            CallData.objects.filter(**search_data_params).values("csv_data")
        )
        query_set = [data.get("csv_data", {}) for data in query_set]
        return Response(data=dict(data=query_set), status=200)

    def bulk_entity_builder(self, data: list):
        return [CallData(csv_data=item) for item in data]

    def senetize_data(self, data: list):
        for d in data:
            for item in d:
                if isinstance(d[item], float):
                    d[item] = None

    def post(self, request, format=None):
        try:
            csv_file = self.request.FILES.get("csv_file")
            df = pd.read_csv(csv_file)
            data = df.to_dict(orient="records")
            # here we will senetize data
            self.senetize_data(data=data)
            with transaction.atomic():
                entities = self.bulk_entity_builder(data=data)
                created = CallData.objects.bulk_create(objs=entities)
                if entities.__len__() == created.__len__():
                    return Response(
                        data={"message": "Data is dumped successfully"}, status=201
                    )
                else:
                    return Response(
                        data={"message": "Data is not dumped try again"}, status=400
                    )

        except Exception as e:
            return Response(
                data={"message": "Data is not dumped try again"}, status=400
            )
