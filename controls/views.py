from django.shortcuts import render
from rest_framework import generics
from tablib import Dataset
from .models import Control
from .serializers import ControlSerializer
from django.http import HttpResponse
from .resources import ControlResource


class ControlList(generics.ListCreateAPIView):
    """Lists all controls and allows you to create more"""
    queryset = Control.objects.all()
    serializer_class = ControlSerializer


class ControlDetail(generics.RetrieveUpdateDestroyAPIView):
    """Grabs a single control and allows you to update it or delete it"""
    queryset = Control.objects.all()
    serializer_class = ControlSerializer


# Export and Import functions make use of the django-import-export library
def export_controls(request):
    """Automatically saves the csv file of your controls in your specified download folder, does not overwrite"""
    control_resource = ControlResource()
    dataset = control_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="controls.csv"'
    return response


def import_controls(request):
    """Takes you to a html page where you can select a file from your computer to upload your control csv"""
    if request.method == 'POST':
        control_resource = ControlResource()
        dataset = Dataset()
        new_controls = request.FILES['myfile']

        imported_data = dataset.load(new_controls.read().decode('utf-8'), format='csv')
        result = control_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            control_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'import.html')
