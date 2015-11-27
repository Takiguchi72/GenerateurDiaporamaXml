import argparse
import os

def obtenirCheminRepertoirePersonnel():
    return os.popen("cd && pwd").read().split("\n")[0]

class Argparser(object):
    # ~~~~~~~~~ #
    # Attributs #
    # ~~~~~~~~~ #
    # self.valeurs.dossier_images
    # self.valeurs.nom
    # self.valeurs.destination
    # self.valeurs.duree
    
    # ~~~~~~~~~~~~ #
    # Constructeur #
    # ~~~~~~~~~~~~ #
    def __init__(self):
        # Initialisation des arguments à l'objet
        self.__ajoutArguments__()
        
        # Récupération des valeurs de la CLI pour les stocker dans l'objet 'valeurs'
        self.valeurs = self.parser.parse_args()
        
        # Si le chemin du dossier d'images finit par un '/', on le supprime
        if(self.valeurs.dossier_images[-1] == "/"):
            self.valeurs.dossier_images = self.valeurs.dossier_images[:-1]
        
        # On attribut des valeurs par défaut aux arguments optionnels non renseignés
        self.__verifierArgumentsOptionnels__()
    
    # ~~~~~~~~ #
    # Méthodes #
    # ~~~~~~~~ #
    '''
    Ajoute les arguments à l'argument parser
    '''
    def __ajoutArguments__(self):
        self.arguments = argparse.Namespace()
        self.parser = argparse.ArgumentParser()
        
        # Ajout des arguments positionnels
        self.parser.add_argument("dossier_images",
                                 help = "Le chemin du dossier contenant les images")
        
        # Ajout des arguments optionnels
        self.parser.add_argument("-n",
                                 "--nom",
                                 nargs = 1,
                                 help = "Spécifie le nom du fichier xml qui sera généré")
        
        self.parser.add_argument("-D",
                                 "--destination",
                                 nargs = 1,
                                 help = "Spécifie le chemin du dossier où le diaporama xml sera généré")

        self.parser.add_argument("-d",
                                 "--duree",
                                 nargs = 1,
                                 help = "Spécifie la durée d'affichage de chaque image du diaporama")
    
    '''
    Attribut des valeurs par défaut aux arguments optionnels non renseignés
    '''
    def __verifierArgumentsOptionnels__(self):
        # Si l'argument "--nom" n'a pas été renseigné,
        # on lui attribut la valeur "fond_d_ecran.xml" comme valeur par défaut
        if(type(self.valeurs.nom).__name__ == "NoneType"):
            self.valeurs.nom = ["fond_d_ecran.xml"]
        else:
            if(not self.valeurs.nom[0][-4:] == ".xml"):
                raise Exception("Le diaporama doit être un fichier xml, dont le nom doit se terminer par l'extension '.xml'.")
           
        # Si l'argument "--destination" n'a pas été renseigné,
        # on lui attribut la valeur "/home/USER" comme valeur par défaut
        if(type(self.valeurs.destination).__name__ == "NoneType"):
            self.valeurs.destination = [obtenirCheminRepertoirePersonnel()]
        else:
            # Si la destination qui a été renseigné se finit par un '/', on l'enlève
            if(self.valeurs.destination[0][-1] == "/"):
                self.valeurs.destination[0] = self.valeurs.destination[0][:-1]
        
        # Si l'argument "--duree" n'a pas été renseigné,
        # on lui attribut la valeur "60" comme valeur par défaut
        if(type(self.valeurs.duree).__name__ == "NoneType"):
            self.valeurs.duree = ["60"]