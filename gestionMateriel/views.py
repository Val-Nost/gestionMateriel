from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from gestionMateriel.form import EnseignantForm
from gestionMateriel.models import Enseignant, Salle


# Create your views here.
def accueil(request):
    return render(request, 'index.html')


########################################################################################
########################################################################################
#############################       Enseignant           ###############################
########################################################################################
########################################################################################
def listeEnseignants(request):
    context = {
        'enseignants': Enseignant.objects.all()
    }
    return render(request, 'enseignant/liste.html', context)


def detailEnseignant(request, enseignantId):
    context = {
        'enseignant': Enseignant.objects.get(pk=enseignantId)
    }
    return render(request, 'enseignant/detail.html', context)


class EnseignantCreateView(CreateView):
    model = Enseignant
    form_class = EnseignantForm
    template_name = 'enseignant/create.html'

    def get_success_url(self):
        return reverse("detailEnseignant", args=[self.object.pk])


########################################################################################
########################################################################################
#############################          Salle             ###############################
########################################################################################
########################################################################################
def listeSalles(request):
    context = {
        'salles': Salle.objects.all()
    }
    return render(request, 'salle/liste.html', context)


def detailSalle(request, salleId):
    context = {
        'salle': Salle.objects.get(pk=salleId)
    }
    return render(request, 'salle/detail.html', context)