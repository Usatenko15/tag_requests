from rest_framework import serializers
from .models import Url_table


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url_table
        fields = ('id','url', 'tags_list', 'time')