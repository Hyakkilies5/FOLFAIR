from Tache import *
from TabTaches import *

#Def du tableau 
liste = TabTaches()

# Exemple de saisie d'une tâche
nouvelle_tache = Tache("", 0, "", "")
nouvelle_tache.saisie()
liste.ajouter_tache(nouvelle_tache)

# Affichage de toutes les tâches
liste.afficher_taches()

