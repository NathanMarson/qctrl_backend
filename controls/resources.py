from import_export import resources
from .models import Control


class ControlResource(resources.ModelResource):
    class Meta:
        model = Control
        exclude = 'id'  # id excluded to match the format of the example csv
