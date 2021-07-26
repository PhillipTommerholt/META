from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from avs.models import Av, Leverandor, Medie, Maskine, Arkivar


@login_required(login_url='login_view')
def overblik(request):
    total = 0
    total_size = 0

    modtaget = Av.objects.filter(status='Modtaget').order_by('svarfrist', 'avid', 'version')
    modtaget_count = len(modtaget)
    total += modtaget_count
    for av in modtaget:
        try:
            size = float(av.storrelse.replace(',', '.'))
        except ValueError:
            size = 0
        total_size += size

    oprettet = Av.objects.filter(status='Oprettet').order_by('svarfrist', 'avid', 'version')
    oprettet_count = len(oprettet)
    total += oprettet_count
    for av in oprettet:
        try:
            size = float(av.storrelse.replace(',', '.'))
        except ValueError:
            size = 0
        total_size += size

    kvitteret = Av.objects.filter(status='Kvitteret').order_by('svarfrist', 'avid', 'version')
    kvitteret_count = len(kvitteret)
    total += kvitteret_count
    for av in kvitteret:
        try:
            size = float(av.storrelse.replace(',', '.'))
        except ValueError:
            size = 0
        total_size += size

    mangler = Av.objects.filter(status='Mangler kodeord').order_by('svarfrist', 'avid', 'version')
    mangler_count = len(mangler)
    total += mangler_count
    for av in mangler:
        try:
            size = float(av.storrelse.replace(',', '.'))
        except ValueError:
            size = 0
        total_size += size

    tilgaengelig = Av.objects.filter(status='Tilgængelig').order_by('svarfrist', 'avid', 'version')
    tilgaengelig_count = len(tilgaengelig)
    total += tilgaengelig_count
    for av in tilgaengelig:
        try:
            size = float(av.storrelse.replace(',', '.'))
        except ValueError:
            size = 0
        total_size += size

    journaliseret = Av.objects.filter(status='Journaliseret').order_by('svarfrist', 'avid', 'version')
    journaliseret_count = len(journaliseret)
    total += journaliseret_count
    for av in journaliseret:
        try:
            size = float(av.storrelse.replace(',', '.'))
        except ValueError:
            size = 0
        total_size += size

    kopieret = Av.objects.filter(status='Kopieret').order_by('svarfrist', 'avid', 'version')
    kopieret_count = len(kopieret)
    kopieret_size = 0
    total += kopieret_count
    for av in kopieret:
        try:
            size = float(av.storrelse.replace(',', '.'))
        except ValueError:
            size = 0
        kopieret_size += size
        total_size += size
    kopieret_size = round(kopieret_size, 2)

    ada = Av.objects.filter(status='Afvikler ADA').order_by('svarfrist', 'avid', 'version')
    ada_count = len(ada)
    ada_size = 0
    total += ada_count
    for av in ada:
        try:
            size = float(av.storrelse.replace(',', '.'))
        except ValueError:
            size = 0
        ada_size += size
        total_size += size
    ada_size = round(ada_size, 2)

    klar = Av.objects.filter(status='Klar til test').order_by('svarfrist', 'avid', 'version')
    klar_count = len(klar)
    klar_size = 0
    total += klar_count
    for av in klar:
        try:
            size = float(av.storrelse.replace(',', '.'))
        except ValueError:
            size = 0
        klar_size += size
        total_size += size
    klar_size = round(klar_size, 2)

    under = Av.objects.filter(status='Under test').order_by('svarfrist', 'avid', 'version')
    under_count = len(under)
    under_size = 0
    total += under_count
    for av in under:
        try:
            size = float(av.storrelse.replace(',', '.'))
        except ValueError:
            size = 0
        under_size += size
        total_size += size
    under_size = round(under_size, 2)

    godkendt = Av.objects.filter(status='Forhåndsgodkendt af tester').order_by('svarfrist', 'avid', 'version')
    godkendt_count = len(godkendt)
    total += godkendt_count
    for av in godkendt:
        try:
            size = float(av.storrelse.replace(',', '.'))
        except ValueError:
            size = 0
        total_size += size

    dea = Av.objects.filter(status='Afvikler DEA').order_by('svarfrist', 'avid', 'version')
    dea_count = len(dea)
    dea_size = 0
    total += dea_count
    for av in dea:
        try:
            size = float(av.storrelse.replace(',', '.'))
        except ValueError:
            size = 0
        dea_size += size
        total_size += size
    dea_size = round(dea_size, 2)

    afleveret = Av.objects.filter(status='Afleveret til DEA').order_by('svarfrist', 'avid', 'version')
    afleveret_count = len(afleveret)
    afleveret_size = 0
    total += afleveret_count
    for av in afleveret:
        try:
            size = float(av.storrelse.replace(',', '.'))
        except ValueError:
            size = 0
        afleveret_size += size
        total_size += size
    afleveret_size = round(afleveret_size, 2)

    parat = Av.objects.filter(status='Parat til godkendelse').order_by('svarfrist', 'avid', 'version')
    parat_count = len(parat)
    total += parat_count
    for av in parat:
        try:
            size = float(av.storrelse.replace(',', '.'))
        except ValueError:
            size = 0
        total_size += size

    total_size = str(round(total_size, 2)).replace('.', ',')

    return render(request, 'avs/overblik.html', {
        'total': total,
        'total_size': total_size,
        'modtaget': modtaget,
        'modtaget_count': modtaget_count,
        'oprettet': oprettet,
        'oprettet_count': oprettet_count,
        'kvitteret': kvitteret,
        'kvitteret_count': kvitteret_count,
        'mangler': mangler,
        'mangler_count': mangler_count,
        'tilgaengelig': tilgaengelig,
        'tilgaengelig_count': tilgaengelig_count,
        'journaliseret': journaliseret,
        'journaliseret_count': journaliseret_count,
        'kopieret': kopieret,
        'kopieret_count': kopieret_count,
        'kopieret_size': kopieret_size,
        'ada': ada,
        'ada_count': ada_count,
        'ada_size': ada_size,
        'klar': klar,
        'klar_count': klar_count,
        'klar_size': klar_size,
        'under': under,
        'under_count': under_count,
        'under_size': under_size,
        'godkendt': godkendt,
        'godkendt_count': godkendt_count,
        'dea': dea,
        'dea_count': dea_count,
        'dea_size': dea_size,
        'afleveret': afleveret,
        'afleveret_count': afleveret_count,
        'afleveret_size': afleveret_size,
        'parat': parat,
        'parat_count': parat_count,
    })
