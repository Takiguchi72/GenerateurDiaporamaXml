from fonctions import afficher

fichier = None

'''
Ouvre le fichier spécifié en paramètres. S'il existe, il sera écrasé, autrement, il sera créé.
@param cheminFichier Le chemin absolu vers le fichier à ouvrir. Ex: "/home/user/fichier.xml"
'''
def ouvrirFichier(cheminFichier):
    global fichier
    try:
        fichier = open(cheminFichier, "w")
        fichier.write("<background>\n")
    except IOError as ex:
        print("Erreur lors de l'ouverture du fichier :\n" + ex.value)
        exit(1)
        
def fermerFichier():
    global fichier
    fichier.write("</background>")
    fichier.close()
    
'''
Ajoute les balises xml permettant d'afficher l'image
@param nomImage Le nom de l'image à ajouter
@param cheminImages Le chemin du dossier contenant les images
@param duree La duree d'affichage de l'image lors du diaporama
'''
def ajouterImage(nomImage, cheminImages, duree):
    global fichier
    fichier.write("  <static>\n")
    fichier.write("    <duration>" + duree + "</duration>\n")
    fichier.write("    <file>" + cheminImages + "/" + nomImage + "</file>\n")
    fichier.write("  </static>\n")
    afficher("Image '" + nomImage + "' ajoutée")