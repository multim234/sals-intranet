from django.shortcuts import render
from .models import Missing


def missing(request):
    """ Page for showing all missings """
    template = "missing.html"
    context = {
            'page_title': "Absences | ",
            'missing': Missing.objects.all(),
            }

    return render(request, template, context)
