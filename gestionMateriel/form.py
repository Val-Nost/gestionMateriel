from django.forms import ModelForm

from gestionMateriel.models import Enseignant, Materiel


class EnseignantForm(ModelForm):
    class Meta:
        model = Enseignant

        fields = (
            "nom",
            "prenom",
        )


class MaterielForm(ModelForm):
    class Meta:
        model = Materiel

        fields = (
            "libelle",
            "budget",
            "acheteur",
            "responsable",
            "possesseur",
            "salle"
        )
