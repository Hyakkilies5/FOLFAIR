import json 
from Tache import *
import copy

class TabTaches:
    def __init__(self):
        self.taches = [] # Crée une liste vide pour stocker les tâches

    def ajouter_tache(self, tache):
        inter = Tache('',0,'','')
        inter = copy.deepcopy(tache)
        self.taches.append(inter)  # Ajoute une tâche à la liste

    def afficher_taches(self):
        for tache in self.taches:
            print(tache)  # Affiche chaque tâche en utilisant sa méthode __str__

    def tri_par_nom(self) :
        self.taches.sort(key=lambda tache: tache.nom)

    def tri_par_priorite(self) :
        self.taches.sort(key=lambda tache: tache.prio, reverse=True)

    def tri_par_date_limite(self) :
        self.taches.sort(key=lambda tache: tache.date_limit)

    def supprimer_tache(self, tache):
        if tache in self.taches:
            self.taches.remove(tache)

    def enregistrer_json(self, nom_fichier):
        liste_taches = [tache.to_dict() for tache in self.taches]
        with open(nom_fichier, 'w') as fichier:
            json.dump(liste_taches, fichier, indent=4)

    def charger_json(self, nom_fichier):
        try:
            with open(nom_fichier, 'r', encoding='utf-8') as fichier:
                liste_taches = json.load(fichier)
                self.taches = [Tache.from_dict(tache_dict) for tache_dict in liste_taches]
        except FileNotFoundError:
            print(f"Fichier '{nom_fichier}' non trouvé. Aucune tâche chargée.")


    
    
