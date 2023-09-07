import base64
import os

from django.conf import settings
from django.core.files.base import ContentFile
from rest_framework import serializers


class Base64FileField(serializers.FileField):
    def to_internal_value(self, source_data: str):
        prefix, source_data = source_data.split(';base64,', 1)
        _, file_extension = prefix.split(':')
        file_name = '.'.join(
            (
                os.urandom(settings.B64ENCODED_FILE_NAME_LENGTH_BYTES).hex(),
                file_extension,
            ),
        )
        file_content_bytes = base64.b64decode(source_data)
        file_content = ContentFile(file_content_bytes, name=file_name)
        return super().to_internal_value(file_content)
