import os

guimode = False
extensions_acceptees = ["png", "jpg"]

'''
Initialise la variable globale 'guimode' à 'True'
'''
def initGuiMode():
    global guimode
    guimode = True


'''
Affiche le message passé en paramètre dans la sortie standard,
uniquement si le mode graphique n'est pas activé.
'''
def afficher(str_message):
    global guimode
    if(not guimode):
        print(str_message)


'''
Vérifie que l'extension passée en paramètre est présente dans la liste des extensions prises en charges
@param str_extension L'extension à vérifier
@return True Si l'extension est dans la liste, False Si l'extension n'est pas dans la liste
'''
def estUneExtensionCorrecte(str_extension):
    global extensions_acceptees
    return str_extension in extensions_acceptees
        

'''
Vérifie qu'un dossier ne contient rien
@param cheminDossier Le chemin absolu du dossier à vérifier
@return True Si le dossier ne contient rien, False Si le dossier contient des fichiers
'''
def estUnDossierVide(str_chemin_dossier):
    if(len(os.popen("ls " + str_chemin_dossier).read().split("\n")) > 1):
        return False
    else:
        return True


'''
Récupère le contenu du dossier en paramètre, sous forme de tableau de chaînes
@param cheminDossier Le chemin absolu vers le dossier récupérer
@raise exception:  Si le dossier est vide
'''
def recupererContenu(str_chemin_dossier):
    contenu = os.popen("ls " + str_chemin_dossier).read().split("\n")
    if(len(contenu) <= 1):
        raise Exception("Le dossier est vide.")
    else:
        return contenu


'''
Vérifie que le fichier n'existe pas à l'endroit précisé en paramètre.
@param cheminFichier Le chemin absolu du dossier où est sensé exister le fichier dit
@param nomFichier Le nom du fichier dont on doit vérifier l'existance
@return True Si le fichier existe, False Si le fichier n'existe pas
'''
def diaporamaExiste(str_chemin_fichier, str_nom_fichier):
    if(len(os.popen("ls " + str_chemin_fichier + " | grep " + str_nom_fichier).read().split("\n")) <= 1):
        return False
    else:
        return True
