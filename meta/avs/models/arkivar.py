from django.db import models


class Arkivar(models.Model):
    navn = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.navn

    class Meta:
        verbose_name_plural = "Arkivarer"
