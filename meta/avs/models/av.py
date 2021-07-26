from django.contrib.auth.models import User
from django.db import models
from .leverandor import Leverandor
from .medie import Medie
from .maskine import Maskine
from .profile import Profile
from .arkivar import Arkivar


class Av(models.Model):
    VERSION = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15),
    )
    KATEGORI = (
        ('Stat', 'Stat'),
        ('Kommune', 'Kommune'),
        ('Privat', 'Privat'),
        ('Klassificeret', 'Klassificeret'),
        ('Forskningsdata', 'Forskningsdata')
    )
    KLASSIFIKATION = (
        ('Ingen', 'Ingen'),
        ('Til tjenestebrug', 'Til tjenestebrug'),
        ('Andet', 'Andet')
    )
    LAND = (
        ('Danmark', 'Danmark'),
        ('Grønland', 'Grønland')
    )
    STATUS = (
        ('Modtaget', 'Modtaget'),
        ('Oprettet', 'Oprettet'),
        ('Kvitteret', 'Kvitteret'),
        ('Mangler kodeord', 'Mangler kodeord'),
        ('Tilgængelig', 'Tilgængelig'),
        ('Journaliseret', 'Journaliseret'),
        ('Kopieret', 'Kopieret'),
        ('Afvikler ADA', 'Afvikler ADA'),
        ('Klar til test', 'Klar til test'),
        ('Under test', 'Under test'),
        ('Tilbagemeldt', 'Tilbagemeldt'),
        ('Afventer genaflevering', 'Afventer genaflevering'),
        ('Forhåndsgodkendt af tester', 'Forhåndsgodkendt af tester'),
        ('Afvikler DEA', 'Afvikler DEA'),
        ('Afleveret til DEA', 'Afleveret til DEA'),
        ('Parat til godkendelse', 'Parat til godkendelse'),
        ('Godkendt', 'Godkendt')
    )
    avid = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    version = models.IntegerField(
        blank=False,
        null=False,
        choices=VERSION,
        default=1,
    )
    jnr = models.CharField(
        max_length=255,
        blank=True
    )
    titel = models.CharField(
        max_length=255,
        blank=True
    )
    kategori = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices=KATEGORI
    )
    klassifikation = models.CharField(
        max_length=255,
        default='in',
        choices=KLASSIFIKATION
    )
    land = models.CharField(
        max_length=255,
        default='dk',
        choices=LAND
    )
    leverandor = models.ForeignKey(
        Leverandor,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    storrelse = models.CharField(
        max_length=255,
        blank=True,
        default=''
    )
    modtaget = models.DateField(
        null=True,
        blank=True,
    )
    kodeord = models.DateField(
        null=True,
        blank=True
    )
    svarfrist = models.DateField(
        null=True,
        blank=True
    )
    svar = models.DateField(
        null=True,
        blank=True
    )
    medier = models.ManyToManyField(
        Medie,
        blank=True,
        related_name='medier'
    )
    maskine = models.ForeignKey(
        Maskine,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    dea_medier = models.ManyToManyField(
        Medie,
        blank=True,
        related_name='dea_medier'
    )
    status = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices=STATUS
    )
    arkivar = models.ForeignKey(
        Arkivar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    tester = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    bliv = models.BooleanField(
        default=False,
    )
    afsluttet = models.BooleanField(
        default=False,
    )
    prioritering = models.IntegerField(
        blank=False,
        null=False,
        default=0,
    )
    antal_arbejdsdage = models.IntegerField(
        blank=False,
        null=False,
        default=0,
    )
    antal_arbejdsdage_med_coronadage = models.IntegerField(
        blank=False,
        null=False,
        default=0,
    )

    public = models.CharField(
        max_length=255,
        blank=True
    )

    def __str__(self):
        return str(self.avid)

    class Meta:
        verbose_name_plural = "Arkiveringsversioner"
