from datetime import datetime

class Tache:
    def __init__(self, nom, prio, description, date_limit):
        self.nom = nom
        self.prio = prio
        self.description = description
        self.date_limit = date_limit
        self.jours_restants = 0

    def __str__(self):
        return f"Tache : {self.nom}\nPriorité : {self.prio}\nDescription : {self.description}\nDate limite : {self.date_limit}\nJours restants :{self.jours_restants}\n"

    def saisie(self):
        print("Nom de la tâche :", end="")
        self.nom = input()
        print("Priorité (1 à 5) :", end="")
        self.prio = int(input())
        print("Description de la tâche :", end="")
        self.description = input()
        while True:
            try:
                print("Date limite (XX/XX/XXXX) :", end="")
                date_limit = input()
                self.date_limit = datetime.strptime(date_limit, "%d/%m/%Y") #FORMAT A RESPECTER : JJ/MM/AAAA
                self.jours_restants = (self.date_limit - datetime.now()).days
                print(end="")
                break
            except ValueError:
                print("Le format de la date doit être XX/XX/XXXX.")
        



