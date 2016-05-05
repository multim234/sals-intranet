from django.contrib import admin
from missing.models import Missing


class MissingAdmin(admin.ModelAdmin):
    list_display = ('staff_name', 'start', 'end')

admin.site.register(Missing, MissingAdmin)
