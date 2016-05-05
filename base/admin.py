from django.contrib import admin
from base.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('texte', 'time_to_show')

admin.site.register(Message, MessageAdmin)
