from .models import Url_table
import datetime
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from .serializers import UrlSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response


class Url_table_View(viewsets.ViewSet):

    def list(self, request):
        queryset = Url_table.objects.all()
        serializer = UrlSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Url_table.objects.all()
        url_id = get_object_or_404(queryset, pk=pk)
        serializer = UrlSerializer(url_id)
        return Response(serializer.data)

    def post(self, request):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; '
                                 'rv:80.0) Gecko/20100101 Firefox/80.0'}
        rs = requests.get(request.POST.get('url'), headers=headers)
        root = BeautifulSoup(rs.content, 'html.parser')
        occurrences = defaultdict(int)
        for tag in root.find_all():
            occurrences[tag.name] += 1
        url_id = Url_table()
        url_id.url = request.POST.get('url')
        url_id.tags_list = occurrences.items()
        url_id.time = datetime.datetime.now()
        url_id.save()
        serializer = UrlSerializer(url_id)
        return Response(serializer.data)



