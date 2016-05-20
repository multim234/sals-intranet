from django.shortcuts import render
from .models import Lunch_menu


def self_menu(request):
    template = "self_menu.html"
    context = {
        'lunch_menu': Lunch_menu.objects.all().order_by('lunch_date')[:7]
    }

    return render(request, template, context)
