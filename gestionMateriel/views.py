from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from gestionMateriel.form import EnseignantForm, MaterielForm, AccessoireForm
from gestionMateriel.models import Enseignant, Salle, Materiel, Accessoire


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
    enseignant = Enseignant.objects.get(pk=enseignantId)
    materielsResponsable = enseignant.responsable.all()
    materielsAchetes = enseignant.acheteur.all()
    materielsPossedes = enseignant.possesseur.all()
    context = {
        'enseignant': enseignant,
        'materielsResponsable':materielsResponsable,
        'materielsAchetes':materielsAchetes,
        'materielsPossedes':materielsPossedes
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
    salle = Salle.objects.get(pk=salleId)
    context = {
        'salle': salle,
        'materiels': salle.materiel_set.all()
    }
    return render(request, 'salle/detail.html', context)


########################################################################################
########################################################################################
#############################          Materiel             ############################
########################################################################################
########################################################################################
def listeMateriels(request):
    context = {
        'materiels': Materiel.objects.all()
    }
    return render(request, 'materiel/liste.html', context)


def detailMateriel(request, materielId):
    materiel = Materiel.objects.get(pk=materielId)
    accessoires = materiel.accessoire_set.all()
    context = {
        'materiel': materiel,
        'accessoires': accessoires
    }
    return render(request, 'materiel/detail.html', context)


class MaterielCreateView(CreateView):
    model = Materiel
    form_class = MaterielForm
    template_name = 'materiel/create.html'

    def get_success_url(self):
        return reverse("detailMateriel", args=[self.object.pk])


########################################################################################
########################################################################################
#############################          Accessoire             ##########################
########################################################################################
########################################################################################

class AccessoireCreateView(CreateView):
    model = Accessoire
    form_class = AccessoireForm
    template_name = 'accessoire/create.html'

    def get_success_url(self):
        return reverse("detailMateriel", args=[self.object.materiel.id])
