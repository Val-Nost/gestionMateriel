from django import forms
from django.forms import ModelForm, Form

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


class TransfertForm(Form):
    nouvelleSalle = forms.MultipleChoiceField(
        widget=forms.Select,
        label="Salle de transfert "
    )

    nouvelEnseignant = forms.MultipleChoiceField(
        widget=forms.Select,
        label="Nouvel enseignant "
    )

    objectif = forms.CharField(max_length=255, label="Raison du transfert ")

    date = forms.DateField(widget=forms.DateInput, label="Date du transfert ")

    accessoirePresent = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label="Accessoires présents "
    )


