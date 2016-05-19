from django.shortcuts import render
from datetime import datetime

# models
from base.models import Message
from missing.models import Missing
from planning_modifications.models import Modification
from self_menu.models import Lunch_menu


def home(request):
    """ Home page view with widgets """
    template = "home.html"
    context = {
            'message': Message.objects.last(),
            'missing': Missing.objects.all()[:5],
            'planning_modification': Modification.objects.all()[:5],
            'lunch_menu': Lunch_menu.objects.filter(lunch_date=datetime.today())
            }

    return render(request, template, context)


def about(request):
    """ About page who show authors,etc... """
    template = "about.html"
    context = {
            'page_title': "A propos | ",
            }
    return render(request, template, context)


def tv_display(request):
    """ home page for tv display """
    template = "tv_display.html"
    context = {
            'message': Message.objects.last(),
            'missing': Missing.objects.all()[:5],
            'planning_modification': Modification.objects.all()[:5],
            }
    return render(request, template, context)
