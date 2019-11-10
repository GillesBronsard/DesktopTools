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
    entry_nameb.delete(0, END) #Efface le champ qui recupere le resultat
    result1 = camelCasifier(entry_name.get())
    entry_nameb.insert(0, result1)
    entry_name.delete(0, END) #Efface le champ d'origine
    
def arboValid():
    try:
        arboDansFic(entry_name2.get())
    except UnicodeEncodeError:
        pass
    entry_name2.delete(0, END) #Efface le champ d'origine
    
def resizeValid():
    resizImage(entry_name3.get(), 2048)
    entry_name3.delete(0, END) #Efface le champ d'origine
    
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
frame1 = Frame(window, bg='#b6b7b8', bd=2, relief=RAISED)

# ajouter un texte à frame1
label_subtitle = Label(frame1, text="CamelCasifieur", font=("Courrier", 20), bg='#b6b7b8', fg='white', width=17)
label_subtitle.grid(row = 0, column=0, ipadx=0, sticky=W)
 
#ajouter un champ à frame1
entry_name = Entry(frame1, width=50)
entry_name.grid(row =1, column=0, padx=10, sticky=EW)

#ajouter un champ2 à frame1
entry_nameb = Entry(frame1, width=27)
entry_nameb.grid(row =2, column=0, padx=10, pady=10, sticky=EW)
 
#ajouter un bouton de validation à frame1
btn = Button(frame1, text="Envoyer", command=camelValid)
btn.grid(row =1, column=1, padx=10, pady=10)
 
# ajouter frame1
frame1.grid(row =0, column=0, pady=10, padx=10, ipady=0, ipadx=0)

#________________________________________________________
# creation frame2
frame2 = Frame(window, bg='#b6b7b8', bd=2, relief=RAISED)

# ajouter un texte à frame2
label_subtitle2 = Label(frame2, text="Arborescence", font=("Courrier", 20), bg='#b6b7b8', fg='white', width=17)
label_subtitle2.grid(row =0, column=0, ipadx=0, sticky =W)

# ajouter un texte à frame2
label_subtitle2 = Label(frame2, text="Crée un fichier Arborescence.txt dans le dossier traité", font=("Courrier", 10), bg='#b6b7b8', fg='white', width=40)
label_subtitle2.grid(row =1, column=0, ipadx=0, sticky =N)

#ajouter un champ à frame2
entry_name2 = Entry(frame2, width=27)
entry_name2.grid(row =2, column=0, padx=10, sticky=EW)

#ajouter un bouton de validation à frame2
btn = Button(frame2, text="Envoyer", command=arboValid)
btn.grid(row =2, column=1, padx=10, pady=10)

# ajouter frame2
frame2.grid(row =1, column=0, pady=10, padx=20, ipady=0, ipadx=0)

#________________________________________________________
# creation frame3
frame3 = Frame(window, bg='#b6b7b8', bd=2, relief=RAISED)

# ajouter un texte à frame2
label_subtitle3 = Label(frame3, text="ResizImage", font=("Courrier", 20), bg='#b6b7b8', fg='white', width=17)
label_subtitle3.grid(row =0, column=0, ipadx=0, sticky =W)

# ajouter un texte à frame3
label_subtitle3 = Label(frame3, text="Resize les photos du dossier traité (non récursif)", font=("Courrier", 10), bg='#b6b7b8', fg='white', width=40)
label_subtitle3.grid(row =1, column=0, ipadx=0, sticky =N)

#ajouter un champ à frame3
entry_name3 = Entry(frame3, width=27)
entry_name3.grid(row =2, column=0, padx=10, sticky=EW)

#ajouter un bouton de validation à frame3
btn = Button(frame3, text="Envoyer", command=resizeValid)
btn.grid(row =2, column=1, padx=10, pady=10)

# ajouter frame3
frame3.grid(row =2, column=0, pady=10, padx=20, ipady=0, ipadx=0)

#________________________________________________________
# afficher
window.mainloop()

