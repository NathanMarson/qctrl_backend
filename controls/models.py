from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Control(models.Model):
    name = models.CharField(max_length=255)

    types = [
        ('Primitive', 'Primitive'),
        ('CORPSE', 'CORPSE'),
        ('Gaussian', 'Gaussian'),
        ('CinBB', 'CinBB'),
        ('CinSK', 'CinSK')]

    type = models.CharField(
        max_length=10,
        choices=types
    )

    # DecimalValidators to ensure the float only goes to 5 decimal places
    maximum_rabi_rate = models.DecimalField(
        decimal_places=5,
        max_digits=8,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    polar_angle = models.DecimalField(
        decimal_places=5,
        max_digits=6,
        validators=[MinValueValidator(0), MaxValueValidator(1)]
    )
