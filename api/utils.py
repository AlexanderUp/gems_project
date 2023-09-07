import base64
import csv
import io

from django.contrib.auth import get_user_model

from gems.models import Customer, Gem

User = get_user_model()


def csv_dict_reader_from_base64(base64_string):
    _, base64_data = base64_string.split(';base64,')
    csv_data_bytes = base64.b64decode(base64_data).decode('utf-8')
    csv_bytes_file = io.StringIO(csv_data_bytes)
    csv_reader = csv.DictReader(csv_bytes_file)
    return csv_reader


def get_gem_instance(gem_name):
    gem, _ = Gem.objects.get_or_create(name=gem_name)
    return gem


def get_user_instance(username):
    user, _ = User.objects.get_or_create(username=username)
    return user


def get_customer_instance(user):
    user, _ = Customer.objects.get_or_create(user=user)
    return user
