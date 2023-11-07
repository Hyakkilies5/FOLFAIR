class TabTaches:
    def __init__(self):
        self.taches = [] # Crée une liste vide pour stocker les tâches

    def ajouter_tache(self, tache):
        self.taches.append(tache)  # Ajoute une tâche à la liste

    def afficher_taches(self):
        for tache in self.taches:
            print(tache)  # Affiche chaque tâche en utilisant sa méthode __str__

    def supprimer_tache(self, tache):
        if tache in self.taches:
            self.taches.remove(tache)
            print(f"Tâche '{tache.nom}' supprimée avec succès.")
        else:
            print(f"Tâche '{tache.nom}' n'a pas été trouvée dans la liste.")