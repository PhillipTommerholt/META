from django.contrib import admin
from .models import Profile, Av, Leverandor, Medie, Maskine, Helligdag, Modtagelse, Arkivar


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'initialer', 'aktiv')
    ordering = ['user']


class AvAdmin(admin.ModelAdmin):
    list_display = ('avid', 'version', 'prioritering', 'titel', 'kategori', 'klassifikation', 'leverandor', 'storrelse', 'status', 'tester', 'maskine', 'afsluttet')
    ordering = ['avid', 'version']


class LeverandorAdmin(admin.ModelAdmin):
    list_display = ('navn',)
    ordering = ['navn']


class MedieAdmin(admin.ModelAdmin):
    list_display = ('navn', 'kapacitet', 'type', 'ibrug')
    ordering = ['navn']


class MaskineAdmin(admin.ModelAdmin):
    list_display = ('navn', 'processor', 'bundkort', 'arbejdshukommelse', 'ibrug')
    ordering = ['navn']


class HelligdagAdmin(admin.ModelAdmin):
    list_display = ('dag', 'corona')
    ordering = ['dag']


class ModtagelseAdmin(admin.ModelAdmin):
    list_display = ('avid',)
    ordering = ['avid']


class ArkivarAdmin(admin.ModelAdmin):
    list_display = ('pk', 'navn')
    ordering = ['navn']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Av, AvAdmin)
admin.site.register(Leverandor, LeverandorAdmin)
admin.site.register(Medie, MedieAdmin)
admin.site.register(Maskine, MaskineAdmin)
admin.site.register(Helligdag, HelligdagAdmin)
admin.site.register(Modtagelse, ModtagelseAdmin)
admin.site.register(Arkivar, ArkivarAdmin)
