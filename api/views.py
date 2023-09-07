import datetime

from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from api.serializers import DealBase64EncodedCSVStringSerializer, DealSerializer
from api.utils import (
    csv_dict_reader_from_base64,
    get_customer_instance,
    get_gem_instance,
    get_user_instance,
)
from gems.models import Customer, Deal, DealPacket, Gem

User = get_user_model()


class DealCreateAPIView(CreateAPIView):
    serializer_class = DealBase64EncodedCSVStringSerializer
    queryset = DealPacket.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        csv_data = serializer.validated_data['csv_data']
        csv_reader = csv_dict_reader_from_base64(csv_data)

        users: dict[str, User] = {}
        customers: dict[str, Customer] = {}
        gems: dict[str, Gem] = {}
        deals: list[Deal] = []

        with transaction.atomic():
            deal_packet = DealPacket.objects.create()
            for row in csv_reader:
                gem_name = row.pop('item')
                customer_name = row.pop('customer')
                date_str = row.pop('date')

                date = datetime.datetime.fromisoformat(date_str)
                date = date.replace(tzinfo=datetime.timezone.utc)

                user = users.setdefault(customer_name, get_user_instance(customer_name))
                customer = customers.setdefault(
                    customer_name,
                    get_customer_instance(user=user),
                )
                gem = gems.setdefault(gem_name, get_gem_instance(gem_name))

                row.update(
                    {
                        'customer': customer,
                        'gem': gem,
                        'deal_packet': deal_packet,
                        'date': date,
                    },
                )
                deals.append(Deal(**row))

            deals = Deal.objects.bulk_create(deals)

        deal_serializer = DealSerializer(deals, many=True)
        return Response(deal_serializer.data, status=status.HTTP_201_CREATED)
