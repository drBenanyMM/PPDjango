from django.shortcuts import render
from django.http import HttpResponse

from personnes.models import Personne

# Create your views here.
def view_personnes(request):
    #return HttpResponse("Test Module Personne")
    personnes = Personne.objects.all()
    return render(request, 'personnes/list.html', context={'personnes': personnes})

 