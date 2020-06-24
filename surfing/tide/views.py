from django.shortcuts import render

# Create your views here.
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView


class ArticleViewT(APIView):
    def get(self, request, key, point):
        import json
        import os
        module_dir = os.path.dirname(__file__)
        file_patch = os.path.join(module_dir, 'Data/')
        with open(file_patch + 'TideList.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
            queryset = json.load(fh)  # загружаем из файла данные в словарь
        if key == 5698456:
            output_dict = [x for x in queryset if x['tide_spot'] == point]
            #resdata = json.dumps(output_dict)
            return Response(output_dict)
        return Response({
            "Error": "Key  incorrect"})
