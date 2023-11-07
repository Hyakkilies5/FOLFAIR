import json
import datetime

class Tache:
    def init(self, nom, prio, description, date_limit):  # Corrigé '__init__'
        self.nom = nom
        self.prio = prio
        self.description = description
        self.date_limit = date_limit

    def affiche(self):
        print("Tache : " + self.nom)
        print("Priorité : " + self.prio)
        print("Description : " + self.description)
        print("Date limite : " + self.date_limit.strftime('%Y-%m-%d'))  # Formatage de la date
        delta = self.date_limit - datetime.datetime.now()
        print("Jours restants : " + str(delta.days))

    # Méthode pour convertir l'objet en un dictionnaire qui peut être sérialisé en JSON
    def dict(self):
        return {
            "nom": self.nom,
            "prio": self.prio,
            "description": self.description,
            "date_limit": self.date_limit.strftime('%Y-%m-%d')  # Convertit l'objet date en string
        }

# Fonction pour sauvegarder la liste des tâches dans un fichier JSON
def save_taches_to_json(taches, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        # Convertit chaque tâche en dictionnaire et les sauvegarde dans le fichier
        json.dump([tache.dict() for tache in taches], f, ensure_ascii=False, indent=4)

# Fonction pour charger la liste des tâches à partir d'un fichier JSON
def load_taches_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        # Crée une liste d'objets Tache à partir des données chargées
        taches_dict = json.load(f)
        return [Tache(d['nom'], d['prio'], d['description'], datetime.datetime.strptime(d['date_limit'], '%Y-%m-%d')) for d in taches_dict]

# Exemple d'utilisation:
taches = [
    Tache("Faire les courses", "Haute", "Acheter du lait et des œufs", datetime.datetime(2023, 12, 25)),
    Tache("Appeler Bob", "Moyenne", "Discuter du rapport", datetime.datetime(2023, 11, 5))
]

# Sauvegarde des tâches dans un fichier
save_taches_to_json(taches, 'taches.json')

# Chargement des tâches à partir du fichier pour vérification
loaded_taches = load_taches_from_json('taches.json')
for tache in loaded_taches:
    tache.affiche()