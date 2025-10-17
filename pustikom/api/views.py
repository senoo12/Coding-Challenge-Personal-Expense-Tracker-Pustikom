from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from rest_framework.response import Response
from .serializers import *

class ExpensesViewSet(viewsets.ModelViewSet):
    # get all data
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializers

    # create filter category
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

    # create pagination 
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
            return response

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'Total Data': queryset.count(),
            'results': serializer.data
        })
