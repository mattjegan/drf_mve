from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from mve.models import Company
from mve.serializers import ExportSerializer

class ExampleViewSet1(GenericViewSet, CreateModelMixin):
    serializer_class = ExportSerializer
