#!/usr/bin/python3.4
#-*- coding: utf-8 -*-

import Argparser
import os
import gestionFichier
import fonctions
from fonctions import afficher, estUneExtensionCorrecte
from gui import FenetrePrincipale

# ~~~~~~~~~~~~~~~~~~~ #
# PROGRAMME PRINCIPAL #
# ~~~~~~~~~~~~~~~~~~~ #
if __name__ == '__main__':
    try:
        # Analyse et stockage des arguments lors de l'appel du programme
        cli = Argparser.Argparser()
        
        if(cli.valeurs.dossier_images == "guimode"):
            fonctions.initGuiMode()
            
            fenetre = FenetrePrincipale.FenetrePrincipale()
            fenetre.run()
        else:
            afficher("\nAnalyse de la ligne de commande...")
            
            # On vérifie que le futur diaporama n'existe pas à l'endroiti choisi par l'utilisateur
            if(fonctions.diaporamaExiste(cli.valeurs.destination[0], cli.valeurs.nom[0])):
                afficher("Le diaporama existe déjà, voulez vous l'écraser ? (O/N)")
                
                saisie = input()
                
                # Si l'utilisateur réponds autre chose que 'O', on quitte le programme
                if(not saisie.upper() == "O"):
                    exit(1)
            
            afficher("Récupération des fichiers...")
            # on récupère le nom des images dans le dossier spécifié
            contenuDossier = fonctions.recupererContenu(cli.valeurs.dossier_images)
             
            uneImageTrouve = False  # Variable permettant de vérifier qu'il y a au moins une image dans le dossier spécifié
             
            afficher("Création du diaporama...")
            gestionFichier.ouvrirFichier(cli.valeurs.destination[0] + "/" + cli.valeurs.nom[0])
             
            # Pour chaque élément du dossier
            for fichier in contenuDossier:
                extension = fichier[-3:]
                # Si l'extension est prise en charge, on ajoute le fichier au diaporama
                if(estUneExtensionCorrecte(extension)):
                    gestionFichier.ajouterImage(fichier, cli.valeurs.dossier_images, cli.valeurs.duree[0])
                    uneImageTrouve = True
             
            # Si aucun fichier du dossier n'était une image prise en charge,
            if(not uneImageTrouve):
                # On supprime le fichier créé précédament
                afficher("Aucune image n'a été trouvé dans le dossier.")
                os.system("rm " + cli.valeurs.destination[0] + "/" + cli.valeurs.nom[0])
            else:
                afficher("Le diaporama a été créé avec succès !\n---> " + cli.valeurs.destination[0] + "/" + cli.valeurs.nom[0])
             
            gestionFichier.fermerFichier()    
            exit(0)
         
    except Exception as ex:
        print("\nErreur :")
        print(ex)
        print("Impossible de générer le diaporama !")
        exit(1)
        