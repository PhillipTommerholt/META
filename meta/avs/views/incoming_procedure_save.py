from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import datetime as dt
import json

from avs.models import Av, Modtagelse, Leverandor, Arkivar, Helligdag, Medie, Maskine


@login_required(login_url='login_view')
def incoming_procedure_save(request):

    avid = request.POST['avid'] if 'avid' in request.POST else None
    version = request.POST['version'] if 'version' in request.POST else None

    m = Modtagelse.objects.filter(avid=avid, version=version).first()

    jnr = request.POST['jnr'] if 'jnr' in request.POST else None
    titel = request.POST['titel'] if 'titel' in request.POST else None
    arkivar = request.POST['arkivar'] if 'arkivar' in request.POST else None
    kategori = request.POST['kategori'] if 'kategori' in request.POST else None
    klassifikation = request.POST['klassifikation'] if 'klassifikation' in request.POST else None
    land = request.POST['land'] if 'land' in request.POST else None
    leverandor = request.POST['leverandor'] if 'leverandor' in request.POST else None
    modtaget = request.POST['modtaget'] if 'modtaget' in request.POST else None
    kodeord = request.POST['kodeord'] if 'kodeord' in request.POST else None
    storrelse = request.POST['storrelse'] if 'storrelse' in request.POST else None
    maskine = request.POST['maskine'] if 'maskine' in request.POST else None

    av = Av.objects.filter(avid=avid, version=version).first()

    av.jnr = jnr if 'h_i_jnr' in request.POST else av.jnr
    av.titel = titel if 'h_i_titel' in request.POST else av.titel
    av.arkivar = Arkivar.objects.filter(navn=arkivar).first() if arkivar else av.arkivar
    av.kategori = kategori if kategori else av.kategori
    av.klassifikation = klassifikation if klassifikation else av.klassifikation
    av.land = land if land else av.land
    av.leverandor = Leverandor.objects.filter(navn=leverandor).first() if leverandor else av.leverandor
    av.storrelse = storrelse if storrelse else av.storrelse

    if 'h_i_modtaget' in request.POST:
        if modtaget == '':
            av.modtaget = None
        else:
            av.modtaget = dt.datetime.strptime(modtaget, '%d.%m.%Y').date()

    if 'h_i_kodeord' in request.POST:
        if kodeord == '':
            av.kodeord = None
            av.svarfrist = None
        else:
            av.kodeord = dt.datetime.strptime(kodeord, '%d.%m.%Y').date()
            av.svarfrist = add_days(av.kodeord, 90)

    m_find_epost = True if 'm_find_epost' in request.POST else False
    m_epost_emne = True if 'm_epost_emne' in request.POST else False
    m_flyt_epost = True if 'm_flyt_epost' in request.POST else False
    m_public = True if 'm_public' in request.POST else False
    m_journalnummer = True if 'm_journalnummer' in request.POST else False
    m_titel = True if 'm_titel' in request.POST else False
    m_arkivar = True if 'm_arkivar' in request.POST else False
    m_enhed = True if 'm_enhed' in request.POST else False
    m_kategori = True if 'm_kategori' in request.POST else False
    m_klassifikation = True if 'm_klassifikation' in request.POST else False
    m_leverandor = True if 'm_leverandor' in request.POST else False
    m_modtaget = True if 'm_modtaget' in request.POST else False
    m_kontakter = True if 'm_kontakter' in request.POST else False
    m_kvittering = True if 'm_kvittering' in request.POST else False
    m_hylde_modtaget = True if 'm_hylde_modtaget' in request.POST else False
    m_find_kodeord = True if 'm_find_kodeord' in request.POST else False
    m_manglende_kodeord = True if 'm_manglende_kodeord' in request.POST else False
    m_kodeord = True if 'm_kodeord' in request.POST else False
    m_journaliser_kodeord = True if 'm_journaliser_kodeord' in request.POST else False
    m_find_epost_modtaget = True if 'm_find_epost_modtaget' in request.POST else False
    m_journaliser_modtaget = True if 'm_journaliser_modtaget' in request.POST else False
    m_slet_epost_modtaget = True if 'm_slet_epost_modtaget' in request.POST else False
    m_find_dokument = True if 'm_find_dokument' in request.POST else False
    m_print_kodeord = True if 'm_print_kodeord' in request.POST else False
    m_luk_medie_op = True if 'm_luk_medie_op' in request.POST else False
    m_bestem_storrelse = True if 'm_bestem_storrelse' in request.POST else False
    m_indtast_storrelse = True if 'm_indtast_storrelse' in request.POST else False
    m_find_sortnet = True if 'm_find_sortnet' in request.POST else False
    m_kopier_av = True if 'm_kopier_av' in request.POST else False
    m_kopieret_hylde = True if 'm_kopieret_hylde' in request.POST else False
    m_placer_kasse = True if 'm_placer_kasse' in request.POST else False

    m.find_epost = m_find_epost if 'h_find_epost' in request.POST else m.find_epost
    m.epost_emne = m_epost_emne if 'h_epost_emne' in request.POST else m.epost_emne
    m.flyt_epost = m_flyt_epost if 'h_flyt_epost' in request.POST else m.flyt_epost
    m.public = m_public if 'h_public' in request.POST else m.public
    m.journalnummer = m_journalnummer if 'h_journalnummer' in request.POST else m.journalnummer
    m.titel = m_titel if 'h_titel' in request.POST else m.titel
    m.arkivar = m_arkivar if 'h_arkivar' in request.POST else m.arkivar
    m.enhed = m_enhed if 'h_enhed' in request.POST else m.enhed
    m.kategori = m_kategori if 'h_kategori' in request.POST else m.kategori
    m.klassifikation = m_klassifikation if 'h_klassifikation' in request.POST else m.klassifikation
    m.leverandor = m_leverandor if 'h_leverandor' in request.POST else m.leverandor
    m.modtaget = m_modtaget if 'h_modtaget' in request.POST else m.modtaget
    m.kontakter = m_kontakter if 'h_kontakter' in request.POST else m.kontakter
    m.kvittering = m_kvittering if 'h_kvittering' in request.POST else m.kvittering
    m.hylde_modtaget = m_hylde_modtaget if 'h_hylde_modtaget' in request.POST else m.hylde_modtaget
    m.find_kodeord = m_find_kodeord if 'h_find_kodeord' in request.POST else m.find_kodeord
    m.manglende_kodeord = m_manglende_kodeord if 'h_manglende_kodeord' in request.POST else m.manglende_kodeord
    m.kodeord = m_kodeord if 'h_kodeord' in request.POST else m.kodeord
    m.journaliser_kodeord = m_journaliser_kodeord if 'h_journaliser_kodeord' in request.POST else m.journaliser_kodeord
    m.find_epost_modtaget = m_find_epost_modtaget if 'h_find_epost_modtaget' in request.POST else m.find_epost_modtaget
    m.journaliser_modtaget = m_journaliser_modtaget if 'h_journaliser_modtaget' in request.POST else m.journaliser_modtaget
    m.slet_epost_modtaget = m_slet_epost_modtaget if 'h_slet_epost_modtaget' in request.POST else m.slet_epost_modtaget
    m.find_dokument = m_find_dokument if 'h_find_dokument' in request.POST else m.find_dokument
    m.print_kodeord = m_print_kodeord if 'h_print_kodeord' in request.POST else m.print_kodeord
    m.luk_medie_op = m_luk_medie_op if 'h_luk_medie_op' in request.POST else m.luk_medie_op
    m.bestem_storrelse = m_bestem_storrelse if 'h_bestem_storrelse' in request.POST else m.bestem_storrelse
    m.indtast_storrelse = m_indtast_storrelse if 'h_indtast_storrelse' in request.POST else m.indtast_storrelse
    m.find_sortnet = m_find_sortnet if 'h_find_sortnet' in request.POST else m.find_sortnet
    m.kopier_av = m_kopier_av if 'h_kopier_av' in request.POST else m.kopier_av
    m.kopieret_hylde = m_kopieret_hylde if 'h_kopieret_hylde' in request.POST else m.kopieret_hylde
    m.placer_kasse = m_placer_kasse if 'h_placer_kasse' in request.POST else m.placer_kasse

    m.save()

    if m.find_epost and m.epost_emne and m.flyt_epost and m.public and m.journalnummer and m.titel and m.arkivar and m.enhed and m.kategori and m.klassifikation and m.leverandor and m.modtaget and m.kontakter and m.kvittering and m.find_kodeord and m.kodeord and m.journaliser_kodeord and m.find_epost_modtaget and m.journaliser_modtaget and m.slet_epost_modtaget and m.find_dokument and m.print_kodeord and m.luk_medie_op and m.bestem_storrelse and m.indtast_storrelse and m.find_sortnet and m.kopier_av and m.kopieret_hylde and m.placer_kasse:
        av.status = "Kopieret"
    elif m.find_epost and m.epost_emne and m.flyt_epost and m.public and m.journalnummer and m.titel and m.arkivar and m.enhed and m.kategori and m.klassifikation and m.leverandor and m.modtaget and m.kontakter and m.kvittering and m.find_kodeord and m.kodeord and m.journaliser_kodeord and m.find_epost_modtaget and m.journaliser_modtaget and m.slet_epost_modtaget:
        av.status = "Journaliseret"
    elif m.find_epost and m.epost_emne and m.flyt_epost and m.public and m.journalnummer and m.titel and m.arkivar and m.enhed and m.kategori and m.klassifikation and m.leverandor and m.modtaget and m.kontakter and m.kvittering and m.find_kodeord and m.kodeord and m.journaliser_kodeord:
        av.status = "Tilgængelig"
    elif m.find_epost and m.epost_emne and m.flyt_epost and m.public and m.journalnummer and m.titel and m.arkivar and m.enhed and m.kategori and m.klassifikation and m.leverandor and m.modtaget and m.kontakter and m.kvittering and m.find_kodeord:
        av.status = "Mangler kodeord"
    elif m.find_epost and m.epost_emne and m.flyt_epost and m.public and m.journalnummer and m.titel and m.arkivar and m.enhed and m.kategori and m.klassifikation and m.leverandor and m.modtaget and m.kontakter and m.kvittering and m.hylde_modtaget:
        av.status = "Kvitteret"
    elif m.find_epost and m.epost_emne and m.flyt_epost and m.public and m.journalnummer and m.titel and m.arkivar and m.enhed and m.kategori and m.klassifikation and m.leverandor and m.modtaget:
        av.status = "Oprettet"
    else:
        av.status = 'Modtaget'

    medier = []
    if 'av_medier' in request.POST:
        _mer = request.POST['av_medier']

        for _m in json.loads(_mer):
            medier.append(_m['tag'].upper())

        av.medier.clear()
        for medie in medier:
            _medie = Medie.objects.filter(navn=medie).first()
            if (_medie):
                av.medier.add(_medie)

    h_maskine = True if 'h_maskine' in request.POST else False

    if h_maskine:
        if maskine and not av.maskine:
            av.maskine = Maskine.objects.filter(navn=maskine).first()
            av.maskine.ibrug += 1
            av.maskine.save()
        elif not maskine and av.maskine:
            av.maskine.ibrug -= 1
            av.maskine.save()
            av.maskine = None

    av.save()

    if 'next' in request.POST:
        if m.status == 'Oprettelse':
            if m.find_epost and m.epost_emne and m.flyt_epost and m.public and m.journalnummer and m.titel and m.arkivar and m.enhed and m.kategori and m.klassifikation and m.leverandor and m.modtaget:
                m.status = request.POST['next_status']
                m.save()

        if m.status == 'Kvittering':
            if m.find_epost and m.epost_emne and m.flyt_epost and m.public and m.journalnummer and m.titel and m.arkivar and m.enhed and m.kategori and m.klassifikation and m.leverandor and m.modtaget and m.kontakter and m.kvittering and m.hylde_modtaget:
                m.status = request.POST['next_status']
                m.save()

        if m.status == 'Kodeord':
            if m.find_epost and m.epost_emne and m.flyt_epost and m.public and m.journalnummer and m.titel and m.arkivar and m.enhed and m.kategori and m.klassifikation and m.leverandor and m.modtaget and m.kontakter and m.kvittering and m.find_kodeord and m.kodeord and m.journaliser_kodeord:
                m.status = request.POST['next_status']
                m.save()

        if m.status == 'Journalisering':
            if m.find_epost and m.epost_emne and m.flyt_epost and m.public and m.journalnummer and m.titel and m.arkivar and m.enhed and m.kategori and m.klassifikation and m.leverandor and m.modtaget and m.kontakter and m.kvittering and m.find_kodeord and m.kodeord and m.journaliser_kodeord and m.find_epost_modtaget and m.journaliser_modtaget and m.slet_epost_modtaget:
                m.status = request.POST['next_status']
                m.save()

        if m.status == 'Kopiering':
            if m.find_epost and m.epost_emne and m.flyt_epost and m.public and m.journalnummer and m.titel and m.arkivar and m.enhed and m.kategori and m.klassifikation and m.leverandor and m.modtaget and m.kontakter and m.kvittering and m.find_kodeord and m.kodeord and m.journaliser_kodeord and m.find_epost_modtaget and m.journaliser_modtaget and m.slet_epost_modtaget and m.find_dokument and m.print_kodeord and m.luk_medie_op and m.bestem_storrelse and m.indtast_storrelse and m.find_sortnet and m.kopier_av and m.kopieret_hylde and m.placer_kasse:
                m.status = request.POST['next_status']
                m.save()

    if 'previous' in request.POST:
        m.status = request.POST['previous_status']
        m.save()

    if 'end' in request.POST and av.status == 'Kopieret':
        m.delete()

    return redirect('incoming_procedure_view', avid, version)


def add_days(start_date, added_days):
    holidays = []

    holiday_objs = Helligdag.objects.all()
    for holiday_obj in holiday_objs:
        holidays.append(holiday_obj.dag)

    days_elapsed = 0
    while days_elapsed < added_days:
        test_date = start_date+dt.timedelta(days=1)
        start_date = test_date
        if test_date in holidays:
            continue
        else:
            days_elapsed += 1

    return start_date
