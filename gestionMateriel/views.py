from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from datetime import date

from gestionMateriel.form import EnseignantForm, MaterielForm, AccessoireForm, TransfertForm
from gestionMateriel.models import Enseignant, Salle, Materiel, Accessoire, Emprunt, Passation, PassationAccessoire


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
        'materielsResponsable': materielsResponsable,
        'materielsAchetes': materielsAchetes,
        'materielsPossedes': materielsPossedes
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
    passations = materiel.passation_set.all()

    context = {
        'materiel': materiel,
        'accessoires': accessoires,
        'passations': passations
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


########################################################################################
########################################################################################
#############################          Transfert             ###########################
########################################################################################
########################################################################################

def transfert(request, materielId):
    if request.method == 'POST':
        materiel = Materiel.objects.get(pk=materielId)
        # On enregistre l'emprunt au reansfert à l'enseignant suivant
        emprunt = Emprunt(
            enseignant=materiel.possesseur,
            date=date.today(),
            salle=materiel.salle
        )
        emprunt.save()

        dateTransfert = request.POST.getlist('date')
        salle = request.POST.getlist('nouvelleSalle')
        enseignant = request.POST.getlist('nouvelEnseignant')
        objectif = request.POST.getlist('objectif')
        accessoires = request.POST.getlist('accessoirePresent')

        passation = Passation(
            datePassation=dateTransfert[0],
            objectif=objectif[0],
            donneur=materiel.possesseur,
            materiel=materiel,
            receveur=Enseignant.objects.get(pk=enseignant[0]),
            lieu=Salle.objects.get(pk=salle[0])
        )
        passation.save()

        for accessoire in accessoires:
            passationAccessoire = PassationAccessoire(
                accessoire=Accessoire.objects.get(pk=accessoire),
                passation=passation
            )
            passationAccessoire.save()
        # redirect
        return HttpResponseRedirect(reverse('detailMateriel', args=[materielId]))
    else:
        materiel = Materiel.objects.get(pk=materielId)
        form = TransfertForm()
        salles = Salle.objects.all()
        form.fields['nouvelleSalle'].choices = [(x.id, x) for x in salles]
        enseignants = Enseignant.objects.all()
        form.fields['nouvelEnseignant'].choices = [(x.id, x) for x in enseignants]
        accessoires = materiel.accessoire_set.all()
        form.fields['accessoirePresent'].choices = [(x.id, x) for x in accessoires]
        return render(request, 'transfert.html', {'form': form})
