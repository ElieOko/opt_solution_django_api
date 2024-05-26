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


class Option(TimeStampModel):
    objects = None
    libelleOption = models.CharField(max_length=100, null=True, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.libelleOption}({self.section.libelleSection})"


class Promotion(TimeStampModel):
    objects = None
    libellePromotion = models.CharField(max_length=100, null=True, blank=True)
    vacationPromotion = models.CharField(max_length=10, null=False, blank=False, choices=vacation)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.libellePromotion}({self.option.libelleOption})'


class Student(TimeStampModel):
    objects = None
    matricule = models.CharField(max_length=255, null=False, blank=True, unique=True)
    nom = models.CharField(max_length=255, null=False, blank=True)
    postnom = models.CharField(max_length=255, null=False, blank=True)
    prenom = models.CharField(max_length=255, null=False, blank=True)
    fk_promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    genre = models.CharField(max_length=10, null=False, blank=True)
    date_de_naissance = models.DateTimeField()

    def __str__(self):
        return f'{self.nom} {self.prenom}'


class TypeFraisAcademique(TimeStampModel):
    objects = None
    nom_frais = models.CharField(max_length=255, null=False, blank=True)


class FraisAcademique(TimeStampModel):
    objects = None
    type_frais_academique = models.ForeignKey(TypeFraisAcademique, on_delete=models.CASCADE)
    nom_frais = models.CharField(max_length=255, null=False, blank=True)
    montant_frais = models.IntegerField(default=1)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nom_frais}({self.promotion})'


class FraisAcademiqueStudent(TimeStampModel):
    objects = None
    frais_academique = models.ForeignKey(FraisAcademique, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status_paiement = models.BooleanField(default=False)


# class GenerateDocumenPaiementStudent(TimeStampModel):
#     student
