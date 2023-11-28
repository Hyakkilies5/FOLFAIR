from tkinter import *
import json

bg = "#7FA0AB"
image_folfair = None
image_barre = None
bg_image = None
change_login_window = None
changement_cesar = 3

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def save_config(login, password):
    encrypted_login = caesar_cipher(login, changement_cesar)
    encrypted_password = caesar_cipher(password, changement_cesar)
    
    config_data = {"login": encrypted_login, "password": encrypted_password}
    
    with open("config.json", "w") as config_file:
        json.dump(config_data, config_file)

def load_config():
    try:
        with open("config.json", "r") as config_file:
            config_data = json.load(config_file)
            decrypted_login = caesar_cipher(config_data["login"], -changement_cesar)
            decrypted_password = caesar_cipher(config_data["password"], -changement_cesar)
            return decrypted_login, decrypted_password
    except FileNotFoundError:
        return "", ""
    
def verify():
    user = entry_login.get()
    passwd = entry_password.get()

    saved_login, saved_password = load_config()

    if user == saved_login and passwd == saved_password:
        titre_connexion.place_forget()
        label_login.place_forget()
        label_password.place_forget()
        entry_login.place_forget()
        entry_password.place_forget()
        button_valider.place_forget()
        page_info()
    else:
        label_access.config(text="ERREUR", font=("Arial", 12, "bold"), bg="black")
        entry_login.delete(0,"end")
        entry_password.delete(0,"end")


def change_login():
    global change_login_window
    change_login_window = Toplevel(window)
    change_login_window.title("Edit Login&Passwd")
    change_login_window.iconbitmap("logo_folfair.ico")
    change_login_window.geometry("300x150")
    change_login_window.resizable(False, False)


    label_new_login = Label(change_login_window, text="Nouvel identifiant:",font=("Courrier", 12, "bold"))
    label_new_password = Label(change_login_window, text="Nouveau mot de passe:",font=("Courrier", 12, "bold"))
    entry_new_login = Entry(change_login_window, font=("Courrier", 12))
    entry_new_password = Entry(change_login_window, show="*", font=("Courrier", 12))

    label_new_login.grid(row=0, column=0, pady=10)
    entry_new_login.grid(row=0, column=1, pady=10)
    label_new_password.grid(row=1, column=0, pady=10)
    entry_new_password.grid(row=1, column=1, pady=10)

    #ici l'utilisation de lambda est obligatoire car on appelle une fonction avec des arguments
    save_button2 = Button(change_login_window, text="Enregistrer", command=lambda: save_new_login_password(entry_new_login.get(), entry_new_password.get()))
    save_button2.grid(row=2, column=0, columnspan=2, pady=10)

def save_new_login_password(new_login, new_password):
    save_config(new_login, new_password)
    change_login_window.destroy()


def ajouter_tache():
    pass
    

def voir_tache():
    def confirmer():
        nb_cadres = spinbox_nb_cadres.get()
        fenetre_dialogue.destroy()
        creer_fenetre_taches(int(nb_cadres))

    def demander_nombre_cadres():
        global fenetre_dialogue
        fenetre_dialogue = Toplevel(window)
        fenetre_dialogue.title("Nombre de tâche")
        fenetre_dialogue.geometry("300x150")
        fenetre_dialogue.resizable(False, False)
        fenetre_dialogue.config(bg="black")
        fenetre_dialogue.iconbitmap("logo_folfair.ico")

        label = Label(fenetre_dialogue, text="Nombre de tâches à afficher:", font=("Courrier", 12, "bold"), bg="black", fg="white")
        label.pack(pady=10)

        global spinbox_nb_cadres
        spinbox_nb_cadres = Spinbox(fenetre_dialogue, from_=1, to=10, width=5, bg="black", fg="white", font=("Courrier", 12, "bold"))
        spinbox_nb_cadres.pack(pady=10)

        bouton_confirmer = Button(fenetre_dialogue, text="Confirmer", command=confirmer, bg="black", fg="white", font=("Courrier", 12, "bold"))
        bouton_confirmer.pack()

    demander_nombre_cadres()

def creer_fenetre_taches(nb_cadres):
    fenetre_taches = Toplevel(window)
    fenetre_taches.title("Liste des tâches")
    fenetre_taches.resizable(True, True)
    fenetre_taches.config(bg="black")
    fenetre_taches.iconbitmap("logo_folfair.ico")

    for i in range(nb_cadres):
        cadre = Frame(fenetre_taches, bg="white", height=500 // nb_cadres, width=1000, borderwidth=1, relief="solid")
        cadre.grid(row=i, column=0, sticky="nsew")

    for i in range(nb_cadres):
        fenetre_taches.grid_rowconfigure(i, weight=1)
    fenetre_taches.grid_columnconfigure(0, weight=1)



#Création de la fenêtre
window = Tk()

#Titre de la fenêtre
window.title("FOLFAIR")

#Taille de la fenêtre

window.geometry("300x250")
window.resizable(False, False)

#Logo de la fenêtre
window.iconbitmap("logo_folfair.ico")

#Background de la page
window.config(bg=bg)




#Creation de widgets page de login

titre_connexion = Label(window, text="CONNEXION", font=("Courrier", 24, "bold"), bg=bg)
label_login = Label(window, text="Utilisateur : ", font=("Arial", 15), bg=bg)
label_password = Label(window, text="Mot de passe : ", font=("Arial", 15), bg=bg)

entry_login = Entry(window, font=("Helvetica", 12), width=18)
entry_password = Entry(window, show="*", font=("Helvetica", 12), width=14)

label_access = Label(window, fg="red", bg=bg)
button_valider = Button(window, text="Valider", font=("Courrier", 12), bg=bg, command=verify)

#Placement des widgets page de login
titre_connexion.place(x=45, y=20)

label_login.place(x=20, y=100)
label_password.place(x=20, y=150)


entry_login.place(x=130, y=105)
entry_password.place(x=165, y=155)

button_valider.place(x = 123, y = 200)

label_access.place(x=20, y=203)


#fonction de la page pour ajouter les informations à mettre dans la todolist

def page_info():
    global image_folfair
    global image_barre
    global bg_image
    global image_barre2

    #config de la page
    bg = "#BFCDF7"

    window.geometry("1200x600")
 
    # Background de la page avec une image
    canvas_bg = Canvas(window, width=1200, height=600)
    canvas_bg.pack()

    # Charger l'image pour le background
    bg_image = PhotoImage(file="fond.png")
    canvas_bg.create_image(0, 0, anchor=NW, image=bg_image)

    width_logo = 160
    height_logo = 150
    
    width_barre = 600
    height_barre = 15

    width_barre2 = 10
    height_barre2 = 338

    image_folfair = PhotoImage(file="logo_folfair.png").zoom(7).subsample(33)
    image_barre = PhotoImage(file="barre_noir.png").zoom(10).subsample(20)

    
    
    

    #widgets
    titre_folfair = Label(window, text="FOLFAIR", font=("Corbel Light", 72, "bold"), bg=bg)

    canvas_logo = Canvas(window, width=width_logo, height=height_logo, bg=bg, bd=0, highlightthickness=0)
    canvas_barre = Canvas(window, width=width_barre, height=height_barre, bg=bg, bd=0, highlightthickness=0)

    nom_tache = Label(window, text = "Nom de la tache:", font=("Helvetica", 24, "bold"), bg=bg)
    prio_tache = Label(window, text = "Priorité (1 à 5): ", font=("Helvetica", 24, "bold"), bg=bg)
    desc_tache = Label(window, text = "Description de la tache: ", font=("Helvetica", 24, "bold"), bg=bg)
    date_limite = Label(window, text = "Date limite (XX/XX/XXXX): ", font=("Helvetica", 24, "bold"), bg=bg)

    entry_nom = Entry(window, font=("Helvetica", 20), width=50, bg="#D4D4EC", fg="#000000")
    entry_prio = Entry(window, font=("Helvetica", 20), width=51, bg="#D4D4EC", fg="#000000")
    entry_desc = Entry(window, font=("Helvetica", 20), width=42, bg="#D4D4EC", fg="#000000")
    entry_date = Entry(window, font=("Helvetica", 20), width=40, bg="#D4D4EC", fg="#000000")

    save_button = Button(window, text="Ajouter tâche", font=("Courrier, 17"), bg="white", fg="black", command=ajouter_tache)

    see_button = Button(window, text="Voir tâches", font=("Courrier, 15"), bg=bg, fg="white", command=voir_tache)

    
    
    #placement des widgets
    titre_folfair.place(x=320, y=10)

    canvas_logo.create_image(width_logo/2, height_logo/2, image=image_folfair)
    canvas_logo.place(x=700, y=0)

    canvas_barre.create_image(width_barre/2, height_barre/2, image=image_barre)
    canvas_barre.place(x=286, y= 130)

    nom_tache.place(x=10, y=200)
    prio_tache.place(x=10, y=300)
    desc_tache.place(x=10, y=400)
    date_limite.place(x=10, y=500)


    entry_nom.place(x=280, y=204)
    entry_prio.place(x=265, y=304)
    entry_desc.place(x=400, y=404)
    entry_date.place(x=430, y=504)


    save_button.place(x= 1045, y=347)
    see_button.place(x=1080, y=10)

    # creation d'une barre de menu

    menu_bar = Menu(window)

    # creer un premier menu

    file_menu = Menu(menu_bar, tearoff=0)

    file_menu.add_command(label="Changer l'identifiant et le mot de passe", command=change_login)
    file_menu.add_command(label="Quitter", command=window.quit)

    menu_bar.add_cascade(label="Fichier", menu=file_menu)

    #configurer la fenetre pour ajouter la menu bar

    window.config(menu=menu_bar)


#Loop de la page principal
window.mainloop()