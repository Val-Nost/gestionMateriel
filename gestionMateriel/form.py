from django.forms import ModelForm

from gestionMateriel.models import Enseignant, Materiel, Accessoire


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


class AccessoireForm(ModelForm):
    class Meta:
        model = Accessoire

        fields = (
            "libelle",
            "etat",
            "materiel"
        )
