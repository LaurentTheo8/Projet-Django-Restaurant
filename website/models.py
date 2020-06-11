from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, date
from django.utils import timezone




# Create your models here.

class Message(models.Model):

    name = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 50)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now, verbose_name="Date of creation")

    class Meta:
        verbose_name = "message"
        ordering = ['date']

    def __str__(self):
        return self.subject


VALIDATE_CHOICES = [
    ('Y', 'validated'),
    ('N', 'not validated'),
  ]

class Reservation(models.Model):

    customer = models.CharField(max_length = 50)
    nbPerson = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    message = models.TextField(null=True, blank=True)
    validate = models.CharField(max_length=1, choices=VALIDATE_CHOICES, default = "N")

    class Meta:
        verbose_name = "reservation"
        ordering = ['validate','date']

    def __str__(self):
        return self.customer
