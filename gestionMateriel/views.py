from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from gestionMateriel.form import EnseignantForm
from gestionMateriel.models import Enseignant


# Create your views here.
def accueil(request):
    return render(request, 'index.html')


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
