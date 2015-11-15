Contexte :
L'environnement Gnome 3 ne dispose pas d'interface pour définir un fond d'écran dynamique (changement d'images toutes les N secondes).
Il est néanmoins possible de définir un fond d'écran dynamique, pour celà il faut disposer d'un fichier xml, respectant une certaine structure, qui contient le chemin absolu des images à afficher comme fond d'écran.

Solution :
Un programme écrit en Python, s'utilisant à la fois en mode ligne de commande et en interface graphique.

Pour activer l'interface graphique, il faut ajouter l'argument "guimode" lors du lancement du programme.

Autrement, il faut définir certains arguments, visibles via "--help".

Une fois le fichier xml généré, il faut aller dans Gnome-tweak-tools, dans la rubrique "Bureau", puis cliquer sur "Emplacement de l'arrière plan" et sélectionner le fichier xml.
