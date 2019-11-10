# -*-coding:Utf-8 -*

"""

Nom du projet : DesktopTools

Date de la derniere revision : 10-11-2019

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
    entry_nameb.delete(0, END) #Efface le champ qui recupere le resultat
    result1 = camelCasifier(entry_name.get())
    entry_nameb.insert(0, result1)
    entry_name.delete(0, END) #Efface le champ d'origine
    
def arboValid():
    try:
        arboDansFic(entry_name.get())
    except UnicodeEncodeError:
        pass
    entry_name.delete(0, END) #Efface le champ d'origine
    
def resizeValid():
    resizImage(entry_name.get(), 2048)
    entry_name.delete(0, END) #Efface le champ d'origine
    
#-------------------------------------------------------
#                        PROGRAMME
#-------------------------------------------------------

# creation fenetre principale
window = Tk()
# personnalisation de la fenetre
window.title("est Tools")
window.geometry("589x261")
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
# creation frame
frame1 = Frame(window, bg='#b6b7b8', bd=2, relief=RAISED)

#ajouter un champ à frame1
entry_name = Entry(frame1, width=90)
entry_name.grid(row =1, column=0, padx=10, pady=10, sticky=EW)

#ajouter un champ2 à frame1
entry_nameb = Entry(frame1, width=90)
entry_nameb.grid(row =2, column=0, padx=10, pady=10, sticky=EW)

# ajouter un texte à frame1
label_subtitle2 = Label(frame1, text="CamelCasifie la chaîne de caractères entrée dans le champ 1 ", font=("Courrier", 11), bg='#b6b7b8', fg='white', width=45)
label_subtitle2.grid(row =3, column=0, padx=10, pady=10, sticky =NW)
 
#ajouter un bouton de validation à frame1
btn = Button(frame1, text="Camel", width=7, command=camelValid)
btn.grid(row =3, column=0, padx=10, pady=10, sticky =E)

# ajouter un second à frame1
label_subtitle2 = Label(frame1, text="Crée un fichier Arborescence.txt dans le dossier traité (champ 1)", font=("Courrier", 11), bg='#b6b7b8', fg='white', width=47)
label_subtitle2.grid(row =4, column=0, padx=10, pady=10, sticky =NW)

#ajouter un bouton de validation à frame1
btn = Button(frame1, text="Arbo", width=7, command=arboValid)
btn.grid(row =4, column=0, padx=10, pady=10, sticky =E)

# ajouter un 3eme texte à frame1
label_subtitle3 = Label(frame1, text="Redimensionne les photos du dossier entrée en champ 1   ", font=("Courrier", 11), bg='#b6b7b8', fg='white', width=45)
label_subtitle3.grid(row =5, column=0, padx=0, pady=0, sticky=W)

#ajouter un bouton de validation à frame1
btn = Button(frame1, text="Resiz", width=7, command=resizeValid)
btn.grid(row =5, column=0, padx=10, pady=10, sticky=E) 

# ajouter frame1
frame1.grid(row =0, column=0, pady=10, padx=10, ipady=0, ipadx=0)

# afficher
window.mainloop()

