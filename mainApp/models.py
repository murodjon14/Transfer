from django.db import models
from django.core.validators import *
from datetime import datetime

class Davlat(models.Model):
    nom = models.CharField(max_length=255)
    def __str__(self):
        return self.nom


class Club(models.Model):
    nom = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='clublar/')
    preidentlar = models.CharField(max_length=255)
    trener = models.CharField(max_length=256)
    t_sana = models.DateField(blank=True, null=True)
    kapital = models.PositiveIntegerField(blank=True, null=True)
    davlat = models.ForeignKey(Davlat, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Positsiya(models.Model):
    nom = models.CharField(max_length=255)
    turi = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nom

class Player(models.Model):
    ism = models.CharField(max_length=60)
    raqam = models.SmallIntegerField(validators=[MaxValueValidator(99)])
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    t_sana = models.DateField(blank=True, null=True)
    moash = models.PositiveIntegerField(blank=True, null=True)
    narx = models.PositiveIntegerField()
    davlat = models.ForeignKey(Davlat, on_delete=models.SET_NULL, null=True)
    pozitsiya = models.ForeignKey(Positsiya, on_delete=models.SET_NULL, null=True)

    def yosh(self):
        hozir = datetime.now().year
        t_yil = int(str(self.t_sana))

        return hozir - t_yil


    def __str__(self):
        return self.ism

