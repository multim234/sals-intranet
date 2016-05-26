from django.contrib import admin
from .models import Modification


class ModificationAdmin(admin.ModelAdmin):
    list_display = ('related_classe', 'related_staff', 'date')

admin.site.register(Modification, ModificationAdmin)
