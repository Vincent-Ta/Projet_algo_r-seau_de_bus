from fastest import *
from foremost import *
from shortest import *
from data2py import dates2dic

class Reseau_de_bus:
    """Represente un réseau de bus sous la forme d'une liste d'arrets (liste d'objets Arret_de_bus"""
    def __init__(self, nom) :
        """Un réseau de bus possède un nom et une liste d'arrets"""
        self.nom=nom
        self.liste_totale_arrets=[]
 

class Arret_de_bus:
    '''
    Classe qyu va représenter les arrets de bus, elle est composée de :
    nom de l'arret 
    Arrets voisin = [arrets_voisin1, arret_voisin2...] -> liste d'objets Arret_de_bus
    ligne = [ligne1, ligne2...] -> liste des lignes pour aller à l'arret voisin qui correspond (ligne1 est un string "ligne 1")
    Horaires=[horaires1, horaires2...] -> à chaque arret voisin correspond une liste d'horaires, ce qui correspond à l'horaire du bus pour aller à l'arret voisin en question
    Horairesjf=[horairesjf1, horairesjf2...] -> de la même manière, à chaque arret voisin correspond une liste d'horaires en weekend et jour férié
    '''

    def __init__(self, nom):
        self.nom = nom
        self.arrets_voisins=[]
        self.ligne=[]
        self.horaires=[]
        self.horaires_jf=[]

    def __str__(self):
        return  "arret : " + self.nom
   
    def add_arret(self, new_arret, new_ligne):
        """Avec cette méthode, on ajoute un arret voisin si celui-ci n'est pas présent dans la liste
        On ajoute aussi à l'arret voisin un arret voisin qui correspond à l'arret"""
        if new_arret not in self.arrets_voisins:
            self.arrets_voisins.append(new_arret)
            new_arret.arrets_voisins.append(self)
            self.ligne.append(new_ligne)
            new_arret.ligne.append(new_ligne)

    def add_horaire(self, horaire):
        """Cette méthode sert à ajouter une liste d'horaires à un arret, IL FAUT LES METTRE DANS LE MÊME ORDRE QUE LES ARRETS"""
        self.horaires.append(horaire)    

    def add_horaire_jf(self, horaire_jf):
        """Cette méthode sert à ajouter une liste d'horaires de weekend à un arret, IL FAUT LES METTRE DANS LE MÊME ORDRE QUE LES ARRETS"""
        self.horaires_jf.append(horaire_jf) 

def meme_nom_dans_la_liste(a, liste):
    """Fonction qui renvoie vraie si l'arret a le meme nom qu'un arret dans une liste (pas forcement memes voisins/horaires)"""
    b=False
    for i in liste :
        if a.nom==i.nom:
            b=True
    return b

def find_object_and_remove(a, liste):
    """Fonction qui permet de trouver un arret dans une liste et de le supprimer"""
    for i in liste :
        if a.nom==i.nom:
            result=i
            liste.remove(i)
            return result

def creation_arrets(data_file_name, ligne, reseau):
    
    """Cette fonction permet à partir du nom d'un fichier contenant des horaires et des noms d'arrtes, de construire le réseau de bus"""
    #un fichier = une ligne de bus
    #La partie suivante a été fournie par les professeurs, elle permet d'ouvrir le fichier et de placer son contenu dans des dictionnaires, plus faciles à manipuler
    try:
        with open(data_file_name, 'r') as f:
            content = f.read()
    except OSError: print("File not found")

    # 'File not found' error message.
        
    #La création des différents dictionnaires avec les horaires et/ou la liste des arrets pour une ligne
    slited_content = content.split("\n\n")
    regular_path = slited_content[0]
    regular_date_go = dates2dic(slited_content[1])
    regular_date_back = dates2dic(slited_content[2])
    we_holidays_path = slited_content[3]
    we_holidays_date_go = dates2dic(slited_content[4])
    we_holidays_date_back = dates2dic(slited_content[5])
    #Fin du code fourni par les professeurs 

    #On initialise une liste d'arrets pour la ligne
    l_arrets=[]
    #l'initialisation d'un arret "terminus" va nous permettre de faire correspondre les arrets et les horaires pour les terminus dde chaque ligne
    terminus=Arret_de_bus("terminus")
 
    #pour chaque élément du dictionnaire des horaires, on crée et ajoute les arrets de bus
    for i in range(len(regular_date_go)):
        #Si un aucun arret de même nom n'est présent dans la liste, on crée et on l'ajoute à la liste
        if meme_nom_dans_la_liste(Arret_de_bus(list(regular_date_go.keys())[i]),reseau.liste_totale_arrets)==False :
            l_arrets.append(Arret_de_bus(list(regular_date_go.keys())[i]))
        #Si un arret du meme nom est présent dans la liste, on supprime l'élémment de la liste totale des arrets avant de l'ajouter à notre liste de la ligne 
        #(cela va servir pour ajouter les arrets voisins juste en parcourant la liste de la ligne)
        else :
            l_arrets.append(find_object_and_remove(Arret_de_bus(list(regular_date_go.keys())[i]),reseau.liste_totale_arrets))
    

    #Pour chaque arret dans la liste de la ligne, on ajoute l'arret suivant en tant qu'arret voisin
    #Pour les extrémités de la ligne de bus, on ajoute l'arret "terminus précédemment créé"
    for j in range(len(l_arrets)): 
        if j==0:
            l_arrets[j].add_arret(terminus, ligne)
            l_arrets[j].add_arret(l_arrets[j+1], ligne)
        elif j==len(l_arrets)-1:
            l_arrets[j].add_arret(terminus, ligne)
        else :
            l_arrets[j].add_arret(l_arrets[j+1], ligne)



    #Chaque arret ayant 2 voisins, il suffit maintenant d'ajouter pour chaque arrets les horaires des bus pour aller vers chaque voisin
    for j in range(len(regular_date_go)):      
        l_arrets[j].add_horaire(list(regular_date_back.values())[len(regular_date_go)-1-j])
        l_arrets[j].add_horaire(list(regular_date_go.values())[j])
        l_arrets[j].add_horaire_jf(list(we_holidays_date_back.values())[len(regular_date_go)-1-j])
        l_arrets[j].add_horaire_jf(list(we_holidays_date_go.values())[j])

    #Il suffit ensuite d'ajouter la liste d'arrets de la ligne à la liste totale du réseau
    reseau.liste_totale_arrets+=l_arrets
 


    