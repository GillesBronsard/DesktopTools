# -*-coding:Latin-1 -*
import os
import string
import glob
import datetime, time
from os import walk, listdir
from os.path import isfile, isdir, join
from PIL import Image

#______________________________________________________________     
#Supprime la ponctuation
def desaccentifier(chaine):
    var2 = 0
    caractAccent = ['ï', 'î', 'é', 'è', 'ê', 'ë', 'à', 'â', 'ä', 'ö', 'ô', 'ù', 'ü', 'É', 'È', 'Ê', 'Ë', 'À', 'Â', 'Ä', 'Ö', 'Ô', 'Ù', 'Ü', 'Ï', 'Î']
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
#print(camelCasifier("Les élèves sont là où ils doivent être !"))

#______________________________________________________________   
  
#On se place dans le dossier souhaité
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

#Retourne le dernier élément du chemin. 
dossierActuel = (os.path.basename(cheminAbs))
#print(dossierActuel)

#______________________________________________________________   

#CamelCasifie un nom de dossier
def Cameldoss(dossAct):
    dossRen = os.rename(dossAct, camelCasifier(dossAct))
    return(dossRen)
#Exemple : 
#camelDoss('test de camelcasification élévation à définir')  
#______________________________________________________________  

#décompose un chemin 
def chemDecomp(chemin):
    chem_split = str.split(chemin, "\\")
    return(chem_split)
#Exemple :
#print(chemDecomp(cheminAbs))    
#______________________________________________________________  

#Crée des dossiers récursifs
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
    print("<br>","Nombre de fichiers trouvés:", len(fichiers), "<br>")
    print("Le {}".format(time.strftime("%d/%m/%Y à %H:%M")))
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
    #print("Nombre de fichiers trouvés:", len(fichiers))
#Exemple   
#allChemRecurs(cheminAbs)

#______________________________________________________________  
#Ecrire les chemins pour toute une arborescence dans un fichier
def arboDansFic(chemin):
    fichiers = glob.glob(os.path.join(chemin, "**"), recursive=True)
    f = open(chemin+"/Arborescence.txt", "w")
    f.write("Arborescence créé le {}".format(time.strftime("%d/%m/%Y à %H:%M"+"\n"+"\n")))
    for fichier in fichiers:
        chemUnParUn = reverseSlash(fichier)
        f.write(chemUnParUn+"\n")
    f.close()
    
#Exemple
#arboDansFic("c:/temp")
#______________________________________________________________
 
#Crée un fichier TXT contenant les dossiers d'un dossier (non recursif)
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
#______________________________________________________________
#Retourne la largeur d'un fichier
def whatWidth (source):
    try:
        maPic = Image.open(source)
        if maPic.size[0] > 8000: 
            pass
        else: 
            return(maPic.size[0])
    except IOError:
        pass
#Exemple    
#print(whatWidth("c:/temp/portrait.jpg"))  
    
#Retourne la hauteur d'un fichier
def whatHeight(source):
    try:  
        maPic = Image.open(source)
        if maPic.size[0] > 8000:
            pass
        else:
            return(maPic.size[1])
    except IOError:
        pass
#Exemple    
#print(whatHeight("c:/temp/portrait.jpg"))  

#______________________________________________________________
#Redimensionner des images en JPG et BMP dans un dossier unique

def resizImage(source, diMax):
    imageFiles = [ f for f in listdir(source) if isfile(join(source,f)) and (f.endswith("JPG") or f.endswith("jpg")) ] #or f.endswith("BMP") or f.endswith("bmp")) ]
    target = int(diMax)
    for im in imageFiles :
        if whatWidth(source+"/"+im)==None or whatWidth(source+"/"+im)==2048 or whatHeight(source+"/"+im)==2048 or whatWidth(source+"/"+im)<2048 and whatHeight(source+"/"+im)<2048:
            pass
        else:
            try:
                im1 = Image.open(join(source,im))
                originalWidth, originalHeight = im1.size
                ratio = originalWidth / originalHeight
                if ratio > 1 :
                    width = target
                    height = int(width / ratio)
                else :
                    height = target
                    width = int(height * ratio)
                im2 = im1.resize((width, height), Image.ANTIALIAS)
                #im2.save(join(source, "".join([str(width),"x",str(height),"_",im]))) #Permet de ne pas ecraser l'original
                im2.save(source+'/'+im)
            except IOError:#Erreur sur les photos panoramiques
                pass
            except FileNotFoundError:
                pass
    try:
        with open("C:/temp/log.log", "a") as fic:
            dossier = source + " : Dossier traité le {}".format(time.strftime("%d/%m/%Y à %H:%M"))
            fic.write("\n"+ str(dossier))
#            fic.write("\n\n"+ str(im)+" redimensionnée")
    except UnboundLocalError:
        print("Le dossier", source, "est vide")

#Exemple
#resizImage("C:/temp/Dossier01/Bureaux Nantes", 2048)

