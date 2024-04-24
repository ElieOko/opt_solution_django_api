from django.db import models


# Create your models here.

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Section(TimeStampModel):
    libelleSection = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.libelleSection


class Promotion(TimeStampModel):
    libellePromotion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.libellePromotion


class Option(TimeStampModel):
    libelleOption = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.libelleOption
