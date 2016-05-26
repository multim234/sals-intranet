from django.contrib import admin
from .models import Lunch_menu


class LunchAdmin(admin.ModelAdmin):
    list_display = ('lunch_date', 'midday_dish', 'dinner_dish')
    fieldsets = (
        (None, {
            'fields': ('lunch_date',)
        }),
        ('Midday', {
            'classes': ('collapse'),
            'fields': ('midday_entrance', 'midday_dish', 'midday_dessert'),
        }),
        ('Dinner', {
            'classes': ('collapse'),
            'fields': ('dinner_entrance', 'dinner_dish', 'dinner_dessert'),
        }),
    )

admin.site.register(Lunch_menu, LunchAdmin)
