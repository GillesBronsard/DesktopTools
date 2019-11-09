# -*-coding:Utf-8 -*

"""

Nom du projet : DesktopTools

Date de la derniere revision : 02-11-2019

Révision N° : Version 1

Client : ProjetPerso

Fichiers du projet :
                    -    main.py
                    
                
"""

#-----------------------------------------------
#            Zone des 'imports' de modules
#-----------------------------------------------

from tkinter import *
from tkinter import messagebox
from ModFilesTools import *

#----------------------------------------------------
#        Zone de déclaration des variables globales
#----------------------------------------------------


#-------------------------------------------------------
#        Zone de déclaration des fonctions
#-------------------------------------------------------

def show_about():
    about_window = Toplevel(window)
    about_window.title("A propos")
    about_window.geometry("250x50")
    about_window.iconbitmap("includes/LogoB.ico")
    lb = Label(about_window, text="Créé le 02-11-2019")
    lb.pack()

def camelValid():
    print("TEST")

#-------------------------------------------------------
#                        PROGRAMME
#-------------------------------------------------------

# creation fenetre principale
window = Tk()

# personnalisation de la fenetre
window.title("est Tools")
window.geometry("720x650")
window.minsize(480, 360)
window.iconbitmap("includes/LogoB.ico")
window.config(background='#fa4616')
window.resizable(width=False, height=False) #Interdit le redimensionnement de la fenêtre

#________________________________________________________
# creation barre de menu
menu_bar = Menu(window)

# creation 1er menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="A propos", command=show_about)
file_menu.add_command(label="Quitter", command=window.quit)

menu_bar.add_cascade(label="Fichier", menu=file_menu)

# configurer la fenetre pour ajouter la barre de menu
window.config(menu=menu_bar)

#________________________________________________________
# creation frame1
frame1 = Frame(window, bg='#b6b7b8', bd=0, relief=SUNKEN)
 
# ajouter un texte à frame1
label_subtitle = Label(frame1, text="Frame1", font=("Courrier", 25), bg='#b6b7b8', fg='white')
label_subtitle.grid(row = 0, column=0, sticky =S)
 
#ajouter un champ à frame1
entry_name = Entry(frame1, width=27)
entry_name.grid(row = 1, column=0, sticky =S)
 
#ajouter un bouton de validation à frame1
btn = Button(frame1, text="Envoyer", command=camelValid)
btn.grid(row =2, column=0, sticky=S)
 
# ajouter frame1
frame1.grid(row =0, column=0, pady=20, padx=0, ipady=0, ipadx=0)

#________________________________________________________
# creation frame2
frame2 = Frame(window, bg='#b6b7b8', bd=0, relief=GROOVE)

# ajouter un texte à frame2
label_subtitle = Label(frame2, text="Frame2", font=("Courrier", 25), bg='#b6b7b8', fg='white')
label_subtitle.grid(row =0, column=0, sticky =S)

#ajouter un champ à frame2
entry_name2 = Entry(frame2, width=27)
entry_name2.grid(row =1, column=0, sticky=E)

#ajouter un bouton de validation à frame2
btn = Button(frame2, text="Envoyer", command=camelValid)
btn.grid(row =2, sticky=S)

# ajouter frame2
frame2.grid(row =1, column=0, pady=10, padx=20, ipady=0, ipadx=0)

#________________________________________________________

# afficher
window.mainloop()

