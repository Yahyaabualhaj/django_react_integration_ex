
from rest_framework import serializers


class VacationSerializer(serializers.Serializer):
    date_from = serializers.DateField()
    date_to = serializers.DateField()
    comments = serializers.CharField(max_length=200)
