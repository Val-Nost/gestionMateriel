"""
URL configuration for miniprojet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from gestionMateriel import views
from gestionMateriel.views import EnseignantCreateView, MaterielCreateView, AccessoireCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='index'),
    # Enseignant
    path('enseignant', views.listeEnseignants, name='listeEnseignants'),
    path('enseignant/<int:enseignantId>', views.detailEnseignant, name='detailEnseignant'),
    path('enseignant/creer', EnseignantCreateView.as_view(), name='createEnseignant'),
    # Salle
    path('salle', views.listeSalles, name='listeEnseignants'),
    path('salle/<int:salleId>', views.detailSalle, name='detailEnseignant'),
    # Matériel
    path('materiel', views.listeMateriels, name='listeMateriels'),
    path('materiel/<int:materielId>', views.detailMateriel, name='detailMateriel'),
    path('materiel/creer', MaterielCreateView.as_view(), name='createMateriel'),
    # Accessoire
    path('accessoire/creer', AccessoireCreateView.as_view(), name='createAccessoire'),

]
