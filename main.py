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

#-------------------------------------------------------
#                        PROGRAMME
#-------------------------------------------------------

# creer une premiere fenetre 
window = Tk()

# personnalisation de la fenetre
window.title("est Tools")
window.geometry("720x650")
window.minsize(480, 360)
window.iconbitmap("includes/LogoB.ico")
window.config(background='#fa4616')
window.resizable(width=False, height=False) #Interdit le redimensionnement de la fenêtre

# creer une frame
frame = Frame(window, bg='#fa4616', bd=0, relief=SUNKEN)

# ajouter la frame
frame.pack(expand=YES)

# creation barre de menu
menu_bar = Menu(window)

# creation 1er menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="A propos", command=show_about)
file_menu.add_command(label="Quitter", command=window.quit)

menu_bar.add_cascade(label="Fichier", menu=file_menu)

# configurer la fenetre pour ajouter la barre de menu
window.config(menu=menu_bar)

# afficher
window.mainloop()

