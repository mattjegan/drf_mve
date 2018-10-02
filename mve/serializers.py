
from rest_framework import serializers
from mve.models import Company

# Ref: https://github.com/encode/django-rest-framework/issues/6193
class ExportSerializer(serializers.Serializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    fields = serializers.DictField(child=serializers.CharField())
