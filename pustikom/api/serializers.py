from .models import *
from rest_framework import serializers


class ExpensesSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expenses
        fields = ['id', 'url', 'amount', 'description', 'category', 'created_at', 'updated_at']