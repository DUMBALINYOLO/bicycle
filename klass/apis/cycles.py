from rest_framework import viewsets, status
from rest_framework.response import Response
from klass.models import Klass
from klass.serializers import KlassListDetailSerializer, KlassCreateUpdateSerializer
from django.core.exceptions import ObjectDoesNotExist


def get_class(slug):
    try:
        cl = Klass.objects.get(slug=slug)
        return cl
    except:
        return 'Class Does Not Exist'


class KlassViewSet(viewsets.ModelViewSet):



    def get_serializer_class(self, *args, **kwargs):
        if self.action in ['create', 'put', 'patch']:
            return KlassCreateUpdateSerializer
        return KlassListDetailSerializer


    def get_queryset(self, *args, **kwargs):
        queryset = Klass.objects.filter(active='YES')
        grade = self.request.query_params.get('grade', None)
        print(grade)
        if grade is not None:
            queryset = queryset.filter(grade=grade)
            print()
        return queryset
