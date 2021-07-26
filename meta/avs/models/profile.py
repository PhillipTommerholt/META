from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    mellemnavn = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Mellemnavn'
    )
    initialer = models.CharField(
        max_length=3,
        blank=True,
        null=True,
        verbose_name='Initialer'
    )
    aktiv = models.BooleanField(
        default=True,
        verbose_name='Aktiv'
    )
    modtagelse = models.BooleanField(
        default=False,
        verbose_name='Modtagelse'
    )

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Profiler"
