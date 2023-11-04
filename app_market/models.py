from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Client(models.Model):
    client_id = models.CharField(max_length=20, primary_key=True, unique=True)
    name = models.CharField(max_length=70)
    brokerage = models.FloatField(
        validators=[
            MinValueValidator(
                0.001,
                message="Please enter a valid value. The two nearest valid values are 0.001 and 10.",
            ),
            MaxValueValidator(
                10,
                message="Please enter a valid value. The two nearest valid values are 0.001 and 10.",
            ),
        ]
    )
    date = models.DateField(default=timezone.now, blank=True)

    def __str__(self):
        # Return the numeric part of client_id as a string
        return str(self.client_id)


class Trade(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    exchange = models.CharField(max_length=20)
    symbol = models.CharField(max_length=20)
    rate = models.FloatField()
    netrate = models.FloatField()
    amount = models.FloatField()
    qty = models.PositiveIntegerField()
    date = models.DateField(default=timezone.now, blank=True)
    status = models.CharField(max_length=10)
