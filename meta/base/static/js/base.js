$(document).ready(function () {

    if (document.getElementById('av_medier')) {
        av_data = JSON.parse($("#av_medier").val());
        $('.chips-initial.av_medier').chips({
            data: av_data,
            onChipAdd: (event, chip) => {
                var chipsData = M.Chips.getInstance($('.av_medier')).chipsData;
                var chipsDataJson = JSON.stringify(chipsData);
                var av_medier = document.getElementById('av_medier');
                av_medier.value = chipsDataJson;
            },
            onChipDelete: () => {
                var chipsData = M.Chips.getInstance($('.av_medier')).chipsData;
                var chipsDataJson = JSON.stringify(chipsData);
                var av_medier = document.getElementById('av_medier');
                av_medier.value = chipsDataJson;
            }
        });
    }

    if (document.getElementById('dea_medier')) {
        dea_data = JSON.parse($("#dea_medier").val());
        $('.chips-initial.dea_medier').chips({
            data: dea_data,
            onChipAdd: (event, chip) => {
                var chipsData = M.Chips.getInstance($('.dea_medier')).chipsData;
                var chipsDataJson = JSON.stringify(chipsData);
                var dea_medier = document.getElementById('dea_medier');
                dea_medier.value = chipsDataJson;
            },
            onChipDelete: () => {
                var chipsData = M.Chips.getInstance($('.dea_medier')).chipsData;
                var chipsDataJson = JSON.stringify(chipsData);
                var dea_medier = document.getElementById('dea_medier');
                dea_medier.value = chipsDataJson;
            }
        });
    }

    if (document.getElementById('maskine')) {
        maskine_data = JSON.parse($("#maskine").val());
        $('.chips-initial.maskine').chips({
            data: maskine_data,
            onChipAdd: (event, chip) => {
                var chipsData = M.Chips.getInstance($('.maskine')).chipsData;
                var chipsDataJson = JSON.stringify(chipsData);
                var maskine = document.getElementById('maskine');
                maskine.value = chipsDataJson;
            },
            onChipDelete: () => {
                var chipsData = M.Chips.getInstance($('.maskine')).chipsData;
                var chipsDataJson = JSON.stringify(chipsData);
                var maskine = document.getElementById('maskine');
                maskine.value = chipsDataJson;
            }
        });
    }


    $('select').formSelect();

    $('.modal').modal({
        onOpenEnd: function () {
            $('#avid_create').focus();
            $('#avid_search').focus();
            $('#avid_incoming_create').focus();
        }
    });

    $('#modtaget, #kodeord, #svarfrist, #svar').datepicker({
        'autoClose': true,
        'format': 'dd.mm.yyyy',
        'firstDay': 1,
        'yearRange': 5,
        'showMonthAfterYear': false,
        'disableWeekends': true,
        'showClearBtn': true,
        'showDaysInNextAndPreviousMonths': true,
        i18n: {
            months: ['januar', 'februar', 'marts', 'april', 'maj', 'juni', 'juli', 'august', 'september', 'oktober', 'november', 'december'],
            monthsShort: ["jan", "feb", "mar", "apr", "maj", "jun", "jul", "aug", "sep", "okt", "nov", "dec"],
            weekdays: ["søndag", "mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag"],
            weekdaysShort: ["søn", "man", "tir", "ons", "tor", "fre", "lør"],
            cancel: '',
            done: '',
            clear: 'Ryd',
            formatSubmit: 'dd.mm.yyyy',
        }
    });

    $(document).on('keydown', function (e) {
        if ((e.metaKey || e.altKey) && (String.fromCharCode(e.which).toLowerCase() === 'n')) {
            $("#av_create").modal('open');
        }
        if ((e.metaKey || e.altKey) && (String.fromCharCode(e.which).toLowerCase() === 's')) {
            $("#av_search").modal('open');
        }
        if ((e.metaKey || e.altKey) && (String.fromCharCode(e.which).toLowerCase() === 'm')) {
            $("#incoming_create").modal('open');
        }
    });

    if (document.getElementById("modtaget_dato")) {
        var modtaget_dato = document.getElementById("modtaget_dato").value;
        var modtaget_datepicker = document.getElementById('modtaget');
        var modtaget_instance = M.Datepicker.getInstance(modtaget_datepicker);
        modtaget_instance.setDate(modtaget_dato);
        modtaget_instance._finishSelection();
    }

    if (document.getElementById("kodeord_dato")) {
        var kodeord_dato = document.getElementById("kodeord_dato").value;
        var kodeord_datepicker = document.getElementById('kodeord');
        var kodeord_instance = M.Datepicker.getInstance(kodeord_datepicker);
        kodeord_instance.setDate(kodeord_dato);
        kodeord_instance._finishSelection();
    }

    if (document.getElementById("svarfrist_dato")) {
        var svarfrist_dato = document.getElementById("svarfrist_dato").value;
        var svarfrist_datepicker = document.getElementById('svarfrist');
        var svarfrist_instance = M.Datepicker.getInstance(svarfrist_datepicker);
        svarfrist_instance.setDate(svarfrist_dato);
        svarfrist_instance._finishSelection();
    }

    if (document.getElementById("svar_dato")) {
        var svar_dato = document.getElementById("svar_dato").value;
        var svar_datepicker = document.getElementById('svar');
        var svar_instance = M.Datepicker.getInstance(svar_datepicker);
        svar_instance.setDate(svar_dato);
        svar_instance._finishSelection();
    }

});
