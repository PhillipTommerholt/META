from django.db import models


class Modtagelse(models.Model):
    avid = models.CharField(
        max_length=255,
    )
    version = models.IntegerField(
        default=1,
    )
    status = models.CharField(
        max_length=255,
        default='Oprettelse',
    )
    find_epost = models.BooleanField(
        default=False,
    )
    epost_emne = models.BooleanField(
        default=False,
    )
    flyt_epost = models.BooleanField(
        default=False,
    )
    public = models.BooleanField(
        default=False,
    )
    journalnummer = models.BooleanField(
        default=False,
    )
    titel = models.BooleanField(
        default=False,
    )
    arkivar = models.BooleanField(
        default=False,
    )
    enhed = models.BooleanField(
        default=False,
    )
    kategori = models.BooleanField(
        default=False,
    )
    klassifikation = models.BooleanField(
        default=False,
    )
    leverandor = models.BooleanField(
        default=False,
    )
    modtaget = models.BooleanField(
        default=False,
    )
    kontakter = models.BooleanField(
        default=False,
    )
    kvittering = models.BooleanField(
        default=False,
    )
    hylde_modtaget = models.BooleanField(
        default=False,
    )
    find_kodeord = models.BooleanField(
        default=False,
    )
    manglende_kodeord = models.BooleanField(
        default=False,
    )
    kodeord = models.BooleanField(
        default=False,
    )
    journaliser_kodeord = models.BooleanField(
        default=False,
    )
    find_epost_modtaget = models.BooleanField(
        default=False,
    )
    journaliser_modtaget = models.BooleanField(
        default=False,
    )
    slet_epost_modtaget = models.BooleanField(
        default=False,
    )
    find_dokument = models.BooleanField(
        default=False,
    )
    print_kodeord = models.BooleanField(
        default=False,
    )
    luk_medie_op = models.BooleanField(
        default=False,
    )
    bestem_storrelse = models.BooleanField(
        default=False,
    )
    indtast_storrelse = models.BooleanField(
        default=False,
    )
    find_sortnet = models.BooleanField(
        default=False,
    )
    kopier_av = models.BooleanField(
        default=False,
    )
    kopieret_hylde = models.BooleanField(
        default=False,
    )
    placer_kasse = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.avid

    class Meta:
        verbose_name_plural = "Modtagelser"
