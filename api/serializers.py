import re

from django.core.exceptions import ValidationError
from rest_framework import serializers

from api.fields import Base64FileField
from gems.models import Customer, Deal


class DealBase64EncodedCSVFileSerializer(serializers.Serializer):
    csv_data = Base64FileField()

    def validate_csv_data(self, csv_data):
        err_msg = 'Wrong data supplied.'
        pattern = r'^data:\w{1,6};base64,'
        compiled_pattern = re.compile(pattern)

        if not isinstance(csv_data, str):
            raise TypeError(err_msg)
        if not re.match(compiled_pattern, csv_data):
            raise ValueError(err_msg)
        return csv_data


class DealBase64EncodedCSVStringSerializer(serializers.Serializer):
    csv_data = serializers.CharField(min_length=1)

    def validate_csv_data(self, csv_content):
        if not csv_content.startswith('data:csv;base64,'):
            raise ValidationError('Wrong data supplied.')
        return csv_content


class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = (
            'pk',
            'deal_packet',
            'customer',
            'gem',
            'total',
            'quantity',
            'date',
        )


class CustomerSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    spent_money = serializers.SerializerMethodField()
    gems = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = (
            'username',
            'spent_money',
            'gems',
        )

    def get_username(self, obj):
        return obj.username

    def get_spent_money(self, obj):
        return obj.spent_money

    def get_gems(self, obj):
        return obj.gems
