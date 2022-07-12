from django.contrib import admin

# Register your models here.
from app_gestion.models import Persona, Vac_Domicilio
admin.site.register(Persona)

admin.site.register(Vac_Domicilio)