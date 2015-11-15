
import gestionFichier
import fonctions
from tkinter.messagebox import askquestion
from tkinter.filedialog import *
from tkinter.simpledialog import askstring, askinteger
from Argparser import obtenirCheminRepertoirePersonnel


class FenetrePrincipale():
    '''
    Initialise les composants de la fenêtre
    '''
    def __init__(self):
        self.valeurDossierImages = ""
        self.valeurDuree = "60"
        self.valeurDestinationDiapo=obtenirCheminRepertoirePersonnel()
        self.valeurNomDiapo="fond_d_ecran.xml"
        
        self.__initialiserVue__()
    
    
    '''
    Affiche la fenêtre
    '''
    def run(self):
        self.fenetre.mainloop()
    
    
    '''
    Initialise les composants graphique de la fenêtre
    '''
    def __initialiserVue__(self):
        self.fenetre = Tk() # On instancie la fenêtre
        self.fenetre.title("Générateur de diaporama xml")
        
        # Première zone
        self.frameOne = Frame(self.fenetre)
        self.frameOne.pack(pady=10)
        
        self.frameDossierImages = Frame(self.frameOne)
        self.frameDossierImages.pack()
        
        self.lblSelectDossierImages = Label(self.frameDossierImages,
                                            text="Sélectionnez le dossier contenant les images :")
        self.lblSelectDossierImages.pack(side=LEFT, padx=10)
        
        self.btnDossierImages = Button(self.frameDossierImages,
                                       text="Parcourir...",
                                       command=self.selectionnerDossierImages)
        self.btnDossierImages.pack(side=RIGHT, padx=10)
        
        self.lblDossierImages = Label(self.frameOne)
        self.lblDossierImages.pack(padx=10, ipadx=3, pady=1)
        
        # Deuxième zone
        self.frameTwo = Frame(self.fenetre)
        self.frameTwo.pack(pady=10)
        
            # Choix de la durée entre les images
        self.frameDuree = Frame(self.frameTwo)
        self.frameDuree.pack()
        
        self.lblDuree = Label(self.frameDuree,
                              text="Durée d'affichage de chaque image :")
        self.lblDuree.pack(side=TOP)
        
        self.lblDureeValeur = Label(self.frameDuree,
                                    text="60",
                                    bg='white')
        self.lblDureeValeur.pack(side=LEFT, padx=40, ipadx=3)

        self.btnDuree = Button(self.frameDuree,
                               text="Modifier",
                               command=self.modifierDuree)
        self.btnDuree.pack(side=RIGHT)

        
        
            # Choix du chemin du diapo
        self.frameCheminDiapo = Frame(self.frameTwo)
        self.frameCheminDiapo.pack()
        
        self.lblCheminDiaporama = Label(self.frameCheminDiapo,
                                        text="Chemin d'enregistrement du diaporama :")
        self.lblCheminDiaporama.pack(side=TOP)
        
        self.lblCheminDiaporamaValeur = Label(self.frameCheminDiapo,
                                              text=self.valeurDestinationDiapo,
                                              bg='white')
        self.lblCheminDiaporamaValeur.pack(side=LEFT, padx=10, ipadx=3)
        
        self.btnCheminDiapo = Button(self.frameCheminDiapo,
                                     text="Modifier",
                                     command=self.modifierCheminDiaporama)
        self.btnCheminDiapo.pack(side=RIGHT, padx=10)
        
            # Choix du nom du diapo
        self.frameNomDiapo = Canvas(self.frameTwo)
        self.frameNomDiapo.pack()
        
        self.lblNomDiaporama = Label(self.frameNomDiapo,
                                     text="Nom du diaporama :")
        self.lblNomDiaporama.pack(side=TOP)
        
        self.lblNomDiaporamaValeur = Label(self.frameNomDiapo,
                                           text=self.valeurNomDiapo,
                                           bg='white')
        self.lblNomDiaporamaValeur.pack(side=LEFT, padx=10, ipadx=3)
        
        self.btnNomDiapo = Button(self.frameNomDiapo,
                                  text="Modifier",
                                  command=self.modifierNomDiapo)
        self.btnNomDiapo.pack(side=RIGHT, padx=10)
        
        # Troisième zone
        self.lblCheminFinal = Label(self.fenetre,
                                    text="Chemin : " + self.valeurDestinationDiapo + "/" + self.valeurNomDiapo)
        self.lblCheminFinal.pack(pady=10, ipadx=3)
        
        self.btnValider = Button(self.fenetre,
                                 text="Valider",
                                 command=self.valider)
        self.btnValider.pack(side=RIGHT, padx=10, pady=5)
        
        self.lblAffichage = Label(self.fenetre,
                                  text="")
        self.lblAffichage.pack(side=BOTTOM, padx=10, pady=10)
    
    
    '''
    Affiche une boîte de dialogue permettant de choisir le repertoire contenant les images à inclure au diaporama
    '''
    def selectionnerDossierImages(self):
        self.valeurDossierImages = askdirectory(title="Sélectionnez le dossier contenant les images :")
        if(not len(self.valeurDossierImages) == 0):
            self.lblDossierImages['text'] = self.valeurDossierImages
            self.lblDossierImages['bg'] = "white"
        else:
            self.lblDossierImages['text'] = ""
            self.lblDossierImages['bg'] = "#d9d9d9"
       
    
    '''
    Affiche une boîte de dialogue permettant de choisir la durée d'affichage de chaque image du diaporama,
    et vérifie que la durée est positive
    '''
    def modifierDuree(self):
        duree = askinteger(title="Durée d'affichage de chaque image", 
                           prompt="Durée d'affichage de chaque image ? (en secondes)")
        
        if(not duree is None):
            if(duree <= 0):
                self.afficherErreur("La durée saisie doit être positive !")
            else:
                self.valeurDuree = str(duree)
                self.lblDureeValeur['text'] = self.valeurDuree
            
    
    '''
    Affiche une boîte de dialogue permettant de choisir le repertoire où sera enregistré le futur diaporama
    '''
    def modifierCheminDiaporama(self):
        self.effacerErreur()
        destinationDiapo = askdirectory(title="Chemin d'enregistrement du diaporama :")
        
        # Si l'utilisateur ne clique pas sur annuler,
        if(not len(destinationDiapo) == 0):
            self.valeurDestinationDiapo = destinationDiapo
            self.lblCheminDiaporamaValeur['text'] = self.valeurDestinationDiapo
            self.majLblChemin()
    
    
    '''
    Affiche une boîte de dialogue permettant de saisir le nom du diaporama, et vérifie que le nom saisi ait l'extension '.xml'
    '''
    def modifierNomDiapo(self):
        self.effacerErreur()
        nomDiapo = askstring(title="Nom du diaporama", prompt="Quel nom voulez-vous donner au fichier xml ?")
        
        # Si l'utilisateur a saisi quelque chose
        if(not type(nomDiapo).__name__ == "NoneType"):
            # Si le nom saisi se termine par '.xml'
            if(not nomDiapo[-4:] == ".xml"):
                self.afficherErreur("Le nom saisi doit se terminer par '.xml' !")
            else:
                self.valeurNomDiapo = nomDiapo
                self.lblNomDiaporamaValeur['text'] = self.valeurNomDiapo
                self.majLblChemin()
    
    
    '''
    Vérifie que l'utilisateur a choisi un dossier contenant des images, et procède à la création du diaporama à l'endroit choisi
    '''
    def valider(self):
        try:
            self.effacerErreur()
            # Si l'utilisateur n'a pas choisi de dossier d'images,
            if(len(self.valeurDossierImages) == 0):
                # On lui affiche une erreur
                raise Exception("Veuillez sélectionner le dossier contenant les images !")
            
            # On vérifie que le futur diaporama n'existe pas à l'endroit choisi par l'utilisateur
            if(fonctions.diaporamaExiste(self.valeurDestinationDiapo, self.valeurNomDiapo)):
                # S'il existe déjà, on demande si l'utilisateur veut l'écraser
                reponse = askquestion(title=None, message="Le diaporama existe déjà, voulez vous l'écraser ?")
                
                # S'il répond "Non", on annule la génération du diaporama
                if(not reponse == "yes"):
                    raise Exception("Génération du diaporama annulée !")
            
            # On génère le diaporama xml
            self.afficherMessage("Récupération des fichiers...")
            # on récupère le nom des images dans le dossier spécifié
            contenuDossier = fonctions.recupererContenu(self.valeurDossierImages)
            
            uneImageTrouve = False  # Variable permettant de vérifier qu'il y a au moins une image dans le dossier spécifié
            
            self.afficherMessage("Création du diaporama...")
            gestionFichier.ouvrirFichier(self.valeurDestinationDiapo + "/" + self.valeurNomDiapo)
                  
            # Pour chaque élément du dossier
            for fichier in contenuDossier:
                extension = fichier[-3:]
                # Si l'extension est prise en charge, on ajoute le fichier au diaporama
                if(fonctions.estUneExtensionCorrecte(extension)):
                    gestionFichier.ajouterImage(fichier, self.valeurDossierImages, self.valeurDuree)
                    uneImageTrouve = True
            
            gestionFichier.fermerFichier()
            
            # Si aucun fichier du dossier n'était une image prise en charge,
            if(not uneImageTrouve):
                # On supprime le fichier créé précédament
                self.afficherMessage("Aucune image n'a été trouvé dans le dossier.")
                os.system("rm " + self.valeurDestinationDiapo + "/" + self.valeurNomDiapo)
            else:
                self.afficherMessage("Le diaporama a été créé avec succès !")
                
        except Exception as ex:
                self.afficherErreur(ex)

    
    '''
    Modifie le texte du label 'Chemin final' avec le chemin d'enregistrement du diaporama
    '''
    def majLblChemin(self):
        self.lblCheminFinal['text']="Chemin : " + self.valeurDestinationDiapo + "/" + self.valeurNomDiapo
        
    
    '''
    Affiche un texte de couleur rouge dans le label d'affichage
    @param str_erreur Le message d'erreur à afficher
    '''
    def afficherErreur(self, str_erreur):
        self.lblAffichage['fg'] = 'red'
        self.lblAffichage['text'] = str_erreur
    
    
    '''
    Efface le contenu du label d'affichage
    '''
    def effacerErreur(self):
        self.lblAffichage['text'] = ""
    
    
    '''
    Affiche un message en vert dans le label d'affichage
    '''
    def afficherMessage(self, str_message):
        self.lblAffichage['fg'] = 'green'
        self.lblAffichage['text'] = str_message
        