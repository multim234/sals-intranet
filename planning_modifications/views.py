from django.shortcuts import render
from .models import Modification


def modifications(request):
    template = "modifications.html"
    context = {
        'page_title': "Modification de planning |",
        'modification':  Modification.objects.all(),
    }
    return render(request, template, context)
