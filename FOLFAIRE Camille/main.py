from Tache import *
from TabTaches import *

#Def du tableau 
liste = TabTaches()

'''nouvelle_tache = Tache('',0,'','')
nouvelle_tache.saisie()
liste.ajouter_tache(nouvelle_tache)
nouvelle_tache.saisie()
liste.ajouter_tache(nouvelle_tache)

liste.afficher_taches()

print("\nDonnées dans Tableau")
liste.afficher_taches()
liste.enregistrer_json('taches.json')

print("Blabla\n")
liste = TabTaches()'''
liste.charger_json("taches.json")
liste.afficher_taches()
liste.tri_prio()
liste.afficher_taches()
