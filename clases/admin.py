from django.contrib import admin
from .models import ClaseKitesurf

@admin.register(ClaseKitesurf)
class ClaseKitesurfAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'duracion_horas', 'precio')
    search_fields = ('titulo',)