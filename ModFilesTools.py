# -*-coding:Latin-1 -*
import os
import string
from os import walk, listdir
from os.path import isfile, isdir, join
import glob
import datetime, time


#______________________________________________________________     
#Supprime la ponctuation
def desaccentifier(chaine):
    var2 = 0
    caractAccent = ['�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�']
    caractDesAccent = ['i', 'i', 'e', 'e', 'e', 'e', 'a', 'a', 'a', 'o', 'o', 'u', 'u', 'e', 'e', 'e', 'e', 'a', 'a', 'a','o', 'o','u', 'u', 'i', 'i']
    for var2 in range(26):
        chaine = chaine.replace(caractAccent[var2], caractDesAccent[var2])
        var2 +=1
    return(chaine)
  
#Met une majuscule au debut de chaque mot
def majusculiser(s):
    return string.capwords(s, ' ')

def camelCasifier(phrase): 
    motEnMaj = desaccentifier(phrase)
    motEnMaj = majusculiser(motEnMaj)
    chaine = motEnMaj.replace(" ", "")
    return(chaine)
#Exemple :
#print(camelCasifier("Les �l�ves sont l� o� ils doivent �tre !"))

#______________________________________________________________   
  
#On se place dans le dossier souhait�
#os.chdir('C:\\Users\\GillesB\\test')
def emplacem(chemin) :
    #chemin = os.path.normpath(chemin)
    lieu = os.chdir(chemin)
    return(lieu)
#emplacem("C:\\temp")
#______________________________________________________________   

#On affiche le chemin absolu actuel
cheminAbs = os.path.abspath(".")
#print(cheminAbs)

#______________________________________________________________   

#Retourne le dernier �l�ment du chemin. 
dossierActuel = (os.path.basename(cheminAbs))
#print(dossierActuel)

#______________________________________________________________   

#CamelCasifie un nom de dossier
def Cameldoss(dossAct):
    dossRen = os.rename(dossAct, camelCasifier(dossAct))
    return(dossRen)
#Exemple : 
#camelDoss('test de camelcasification �l�vation � d�finir')  
#______________________________________________________________  

#d�compose un chemin 
def chemDecomp(chemin):
    chem_split = str.split(chemin, "\\")
    return(chem_split)
#Exemple :
#print(chemDecomp(cheminAbs))    
#______________________________________________________________  

#Cr�e des dossiers r�cursifs
def dossRecurs(racine, ajoutDoss):
    arbo = os.makedirs(racine + ajoutDoss)
    return(arbo)
#Exemple
# ajDossier = "\\zzzzz\\iiiii\\ppppp"
# dossRecurs(cheminAbs, ajDossier)
#______________________________________________________________  

#Liste tout les fichiers d'un dossier et de ces sous-dossiers
def listFichiersRecurs(Dossier):
    listeFichiers = []
    for (repertoire, sousRepertoires, fichiers) in walk(Dossier):
        listeFichiers.extend(fichiers)
    return(listeFichiers)
#Exemple :   
#print(listFichiersRecurs(cheminAbs))

#______________________________________________________________  

#Retourne un chemin pour tout les fichiers d'un dossier et de ces sous-dossiers
def chemFichRecurs(Chemin, extens='*') :
#def chemFichRecurs(Chemin) :
    fichiers = glob.glob(os.path.join(Chemin, "**", "*."+extens), recursive=True)
    for fichier in fichiers:
        if isfile(fichier):
            print(fichier, "<br>")
    print("<br>","Nombre de fichiers trouv�s:", len(fichiers), "<br>")
    print("Le {}".format(time.strftime("%d/%m/%Y � %H:%M")))
    return('')
        
#Exemple   
#chemFichRecurs("C:\\Users\\111111111\\Downloads")

#______________________________________________________________  

#Remplace les \ par des /
def reverseSlash(chaine):
    var2 = 0
    backSla = ['\\', '\t', '\n', '/n']
    slashi = ['/', '/t', '/n', '']
    for var2 in range(4):
        chaine = chaine.replace(backSla[var2], slashi[var2])
        var2 +=1
    return(chaine)
#Exemple
#print(reverseSlash("C:\temp\Dossier01\Dossier 01 02"))

#______________________________________________________________  
#Retourne les chemins pour toute une arborescence
def allChemRecurs(Chemin) :
    fichiers = glob.glob(os.path.join(Chemin, "**"), recursive=True)
    for fichier in fichiers:
        chemUnParUn = reverseSlash(fichier)
        print(chemUnParUn, "<br>")
    return('')
    #raise ValueError(f"Le chemin : {Chemin} n'est pas valide")
    #return("")
        
    #Pour afficher le nombre de fichiers :
    #print("Nombre de fichiers trouv�s:", len(fichiers))
#Exemple   
#allChemRecurs(cheminAbs)

#______________________________________________________________  
#Ecrire les chemins pour toute une arborescence dans un fichier
def arboDansFic(chemin):
    fichiers = glob.glob(os.path.join(chemin, "**"), recursive=True)
    f = open(chemin+"/Arborescence.txt", "w")
    f.write("Arborescence cr�� le {}".format(time.strftime("%d/%m/%Y � %H:%M"+"\n"+"\n")))
    for fichier in fichiers:
        chemUnParUn = reverseSlash(fichier)
        f.write(chemUnParUn+"\n")
    f.close()
    
#Exemple
#arboDansFic("c:/temp")
#______________________________________________________________
 
#Cr�e un fichier TXT contenant les dossiers d'un dossier (non recursif)
def listDossDansFic(chemin):
    dossiers = glob.glob(os.path.join(chemin, "**"), recursive=False)
    f = open(chemin+"/Liste_Dossiers.txt", "w")
    for dossier in dossiers:
        if isdir(dossier):
            chemUnParUn = reverseSlash(dossier)
            f.write(chemUnParUn+"\n")
    f.close()
    
#Exemple
#listDossDansFic("C:/Users/GillesB/test")
#______________________________________________________________
#Lire un fichier
def lectFic(chemFichier) :
    fic = open(chemFichier, "r")
    for ligne in fic:
        print(ligne)
    return(ligne)
    fic.close()
#Exemple
#lectFic("S:/monFichier.txt")
