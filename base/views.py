from django.shortcuts import render
from base.models import Message
from missing.models import Missing
from planning_modifications.models import Modification

def home(request):
    """ Home page view with widgets """
    template = "home.html"
    context = {
            'message': Message.objects.last(),
            'missing': Missing.objects.all()[:5],
            'planning_modification': Modification.objects.all()[:5],
            }
    return render(request, template, context)


def about(request):
    """ About page who show authors,etc... """
    template = "about.html"
    context = {
            'page_title': "Auteurs | ",
            }
    return render(request, template, context)
