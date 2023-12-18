from django.shortcuts import render


from . Bdd_personnes import personnes, patients, medecins

def view_contact(request):
    return render(request, 'contact.html')

def view_accueil(request):
    return render(request, 'index.html', context={'personnes':personnes})

    
    
    
    #return render(request, 'index.html')

