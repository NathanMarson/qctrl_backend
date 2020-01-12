from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .serializers import ControlSerializer
from .models import Control
from django.conf.urls import url


# Create your tests here.

client = Client


class ControlTest(TestCase):

    def setUp(self):
        Control.objects.create(
            name='Primary Control', type='Primitive', maximum_rabi_rate='0', polar_angle='0')
        Control.objects.create(
            name='Secondary Control', type='CORPSE', maximum_rabi_rate='100', polar_angle='1')
        Control.objects.create(
            name='Tertiary Control', type='Primitive', maximum_rabi_rate='12.34567', polar_angle='0.12345')

    def test_get_all_controls(self):
        # TODO get tests operational
        response = client.get(reverse('control-list'), url)
        controls = Control.objects.all()
        serializer = ControlSerializer(controls, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
