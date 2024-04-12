from django.forms import ModelForm

from gestionMateriel.models import Enseignant


class EnseignantForm(ModelForm):
    class Meta:
        model = Enseignant

        fields = (
            "nom",
            "prenom",
        )
