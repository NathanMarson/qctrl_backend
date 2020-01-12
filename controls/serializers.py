from rest_framework_json_api import serializers

from .models import Control


class ControlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Control
        fields = '__all__'  # just in case extra fields are added in the future, better than specifying each field
