from tkinter import *

#créer une première fenêtre
window = Tk()

#Personnalisation de la fenêtre
# #Titre
window.title("FOLFAIR")
#Taille
window.geometry("1200x600")
window.resizable(False, False)
#icone
window.iconbitmap("logo_folfair.ico")
#configurer le background
window.config(background='#e9e7fa')

# creer la frame (boite)

frame = Frame(window, bg ="#e9e7fa")

#ajout d'un texte
label_title = Label(window, text = "Bienvenue l'ekip sur FOLFAIR",font=("Courrier", 40), bg="#e9e7fa", fg="black")
label_title.pack(side = TOP)

#ajout d'un second text

label_subtitle = Label(frame, text = "youpi ii",font=("Courrier", 15),bg="#e9e7fa", fg="black")
label_subtitle.pack()

#Ajouter la frame
frame.pack(expand=TRUE)


#afficher la fênetre via la boucle. (donc on utilise la methode main loop)
window.mainloop() 