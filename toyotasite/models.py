from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Car(models.Model):
    BRAND_CHOICES = [
        ('Toyota', 'Toyota'),
    ]

    ENGINE_TYPE_CHOICES = [
        ('diesel', 'Diesel'),
        ('petrol', 'Petrol'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
    ]

    BODY_TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('hatchback', 'Hatchback'),
        ('suv', 'SUV'),
        ('coupe', 'Coupe'),
        ('kombi', 'Kombi'),
        ('van', 'Van'),
    ]

    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    model = models.CharField(max_length=50)
    engine_power = models.IntegerField()
    engine_type = models.CharField(max_length=50, choices=ENGINE_TYPE_CHOICES)
    body_type = models.CharField(max_length=50, choices=BODY_TYPE_CHOICES, default='')
    door_count = models.IntegerField()
    colors = models.ManyToManyField(Color)
    image = models.ImageField(upload_to='photos/', default='')

    def __str__(self):
        return f'{self.brand} {self.model}'
