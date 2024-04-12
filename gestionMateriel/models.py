from django.db import models


# Create your models here.
class Enseignant(models.Model):
    nom = models.CharField(
        verbose_name="Nom",
        help_text="Nom de l'enseignant",
        max_length=255
    )
    prenom = models.CharField(
        verbose_name="Prénom",
        help_text="Prénom de l'enseignant",
        max_length=255
    )

    def __str__(self):
        return self.nom + ' ' + self.prenom


class Salle(models.Model):
    libelle = models.CharField(
        verbose_name="Salle",
        help_text="Salle de cours",
        max_length=255
    )
    batiment = models.CharField(
        verbose_name="Bâtiment",
        help_text="Bâtiment de cours",
        max_length=255
    )
    etage = models.CharField(
        verbose_name="Etage",
        help_text="Etage du bâtiment",
        max_length=255
    )


class Materiel(models.Model):
    libelle = models.CharField(
        verbose_name="Libelle",
        help_text="Libellé du matériel",
        max_length=255
    )
    budget = models.CharField(
        verbose_name="Budget",
        help_text="Budget utilisé",
        max_length=255
    )
    salle = models.ForeignKey(
        Salle,
        verbose_name="Salle",
        help_text="Position du matériel",
        on_delete=models.DO_NOTHING
    )
    responsable = models.ForeignKey(
        Enseignant,
        verbose_name="Responsable",
        help_text="Responsable du matériel",
        related_name="responsable",
        on_delete=models.DO_NOTHING
    )
    acheteur = models.ForeignKey(
        Enseignant,
        verbose_name="Acheteur",
        help_text="Acheteur du matériel",
        related_name="acheteur",
        on_delete=models.DO_NOTHING
    )
    possesseur = models.ForeignKey(
        Enseignant,
        verbose_name="Possesseur",
        help_text="Possesseur du matériel",
        related_name="possesseur",
        on_delete=models.DO_NOTHING
    )


class Accessoire(models.Model):
    libelle = models.CharField(
        verbose_name="Libelle",
        help_text="Libellé de l'accessoire",
        max_length=255
    )
    etat = models.CharField(
        verbose_name="Etat",
        help_text="Etat de l'accessoire",
        max_length=255
    )
    materiel = models.ForeignKey(
        Materiel,
        verbose_name="Matériel de l'accessoire",
        on_delete=models.DO_NOTHING
    )


class Passation(models.Model):
    lieu = models.ForeignKey(
        Salle,
        verbose_name="Salle",
        help_text="Salle d'échange du matériel",
        on_delete=models.DO_NOTHING
    )
    datePassation = models.DateField(
        verbose_name="Date de passation",
        help_text="Date de passation"
    )
    objectif = models.CharField(
        verbose_name="Objectif",
        help_text="Objectif",
        max_length=255
    )
    materiel = models.ForeignKey(
        Materiel,
        verbose_name="Matériel",
        help_text="Matériel échangé",
        on_delete=models.DO_NOTHING
    )
    donneur = models.ForeignKey(
        Enseignant,
        verbose_name="Donneur",
        help_text="Enseignant donnant le matériel",
        related_name="donneur",
        on_delete=models.DO_NOTHING
    )
    receveur = models.ForeignKey(
        Enseignant,
        verbose_name="Receveur",
        help_text="Enseignant recevant le matériel",
        related_name="receveur",
        on_delete=models.DO_NOTHING
    )
