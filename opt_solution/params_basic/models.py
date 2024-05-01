from django.db import models

from .constante import vacation


# Create your models here.

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Section(TimeStampModel):
    objects = None
    libelleSection = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.libelleSection


class Promotion(TimeStampModel):
    objects = None
    libellePromotion = models.CharField(max_length=100, null=True, blank=True)
    vacationPromotion = models.CharField(max_length=10, null=False, blank=False, choices=vacation)

    def __str__(self):
        return self.libellePromotion


class Option(TimeStampModel):
    objects = None
    libelleOption = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.libelleOption
