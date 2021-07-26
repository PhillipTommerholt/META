from django.db import models


class Maskine(models.Model):
    navn = models.CharField(
        max_length=255,
    )

    processor = models.CharField(
        max_length=255,
        default=''
    )

    bundkort = models.CharField(
        max_length=255,
        default=''
    )

    arbejdshukommelse = models.IntegerField(
        default=0,
        verbose_name="Arbejdshukommelse i GB"
    )
    ibrug = models.IntegerField(
        blank=False,
        null=False,
        default=0
    )

    def __str__(self):
        return self.navn

    class Meta:
        verbose_name_plural = "Maskiner"
