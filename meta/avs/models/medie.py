from django.db import models


class Medie(models.Model):
    TYPE = (
        ('Solid State Drive', 'Solid State Drive'),
        ('USB Stick', 'USB Stick'),
        ('Hard Drive 3.5', 'Hard Drive 3.5'),
        ('Hard Drive 2.5', 'Hard Drive 2.5'),
        ('Ekstern SSD USB', 'Ekstern SSD USB'),
    )
    navn = models.CharField(
        max_length=255,
        default=''
    )
    producent = models.CharField(
        max_length=255,
        default=''
    )
    kapacitet = models.IntegerField(
        default=0,
        verbose_name="Kapacitet i GB"
    )
    type = models.CharField(
        max_length=255,
        choices=TYPE
    )
    ibrug = models.IntegerField(
        blank=False,
        null=False,
        default=0
    )

    def __str__(self):
        return self.navn

    class Meta:
        verbose_name_plural = "Medier"
