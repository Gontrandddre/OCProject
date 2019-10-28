Projet 3: Aidez MacGyver à s'échapper !

Projet n°3 du parcours « développeur d’application – Python » chez Openclassrooms. Première mise en application du langage Python à travers la réalisation d’un jeu vidéo en 2D à l’aide de la bibliothèque Pygame. 

Date de réalisation: septembre 2019 - octobre 2019
Lien Github: https://github.com/Gontrandddre/Project3_MacGyver


1. L’environnement & Cahier des charges :

Environnement : 

	- langage: Python 
	- bibliothèque: Pygame, 
	- éditeur de texte: Sublime Text, 
	- outil de versionnage: GIT, 
	- outils d’audit: Pylint & Flake8, 
	- outil de communication: GitHub,
	- solution d’environnement virtuel: VirtualEnv.

Cahier des charges :

Ce jeu doit comporter divers éléments et différentes fonctionnalités. 
Le personnage principale, MacGyver, se dirige sur la structure du labyrinthe grâce aux touches directionnelles, il doit ramasser des objets disposés aléatoirement puis les présenter au gardien qui demeure immobile.  


2. La structure :

	3 fichiers inspirés du modèle MVC (Modèle Vue Contrôleur) : « classes.py » (caractéristiques des éléments du jeu), 
« constantes.py » (gestion des constantes du jeu), 
« mglabyrinth.py » (logique de jeu).

	3 dossiers supports:
"Images"(visuel du labyrinthe et éléments)
"Map" (structure du labyrinthe)
"Sounds"(sons du jeu)

	2 fichiers supports:
"Requirements" (versions des bibliothèques utilisées)
".gitignore" (dossiers/fichiers à ignorer pour git)


3. Les algorithmes :

Gestion des boucles du programme :

	La boucle d’accueil « HOME » permet à l’utilisateur de jouer en appuyant sur la touche « ESPACE ».  Il peut également quitter le programme en appuyant sur la touche « ESCAPE ».  Si l’utilisateur lance le jeu, la boucle « HOME » se fermera pour laisser place à la boucle « PLAY » qui suit.

	La boucle de jeu « PLAY » génère l’ensemble des éléments dans le labyrinthe et sa structure. L’utilisateur pourra donc déplacer MacGyver pour récupérer les objets ou non et gagner la partie ou non. À tout moment l’utilisateur peut quitter le jeu en appuyant sur la touche « ESCAPE ».

Génération de la structure du labyrinthe :

Comme nous l’avons vu précédemment, la structure du labyrinthe se base sur un fichier.txt qui contient 15 lignes et 15 caractères (« m » = mur, « a » = arrivée, « d » = départ, « gardien ») par ligne. 
Pour générer et afficher le labyrinthe nous avons une classe « Labyrinthe » ayant comme attributs dans son constructeur une grille vide ainsi que le fichier.txt. On distingue deux méthodes : 

	Méthode « generate » : Elle génère une liste de listes à partir du fichier.txt. Celle-ci sera intégrée dans la grille vide.

	Méthode « display » : Pour chaque élément de la grille (c’est à dire les caractères), nous allons attribuer un sprite et une position (x, y). Afin que ces sprites soient uniformes et dimensionnés aux caractéristiques du labyrinthe, nous appliquons sur chaque image une fonction « pygame.transform.scale ». Rien n’est affiché pour les cases vides (« 0 »). 

Déplacement et affichage de MacGyver :

Ici, une classe « Hero » est créée pour définir les caractéristiques du personnage MacGyver, elle a comme attributs les coordonnées (x, y) en pixels. Puis, une méthode « move » détient en paramètre la grille du labyrinthe ainsi que la direction à appliquer au personnage.

Dans la boucle du jeu, pour chaque pression d’une touche directionnelle, le personnage se déplacera d’une case dans la direction souhaitée, à condition de rester dans le cadre et de ne pas se confronter à un mur. Afin que l’utilisateur voit le déplacement, un rafraîchissement graphique du labyrinthe sera effectué.

Gestion des objets :

Comme pour la classe « Hero », la classe « Items » a comme attributs les coordonnées (x, y) ainsi que le statut « collected ». Dans cette classe, une méthode pour un affichage aléatoire dans le labyrinthe est prévue. Puis, une seconde méthode permettant de savoir si l’objet a été collecté ou non par MacGyver, est présente.

	Méthode « locate_items » : À travers cette méthode nous créons une liste de l’ensemble des coordonnées possibles sur les cases vides de la grille du labyrinthe. Une fois que la liste des coordonnées est exhaustive, nous appliquons une fonction « random.sample » pour attribuer à chaque objet des coordonnées (x, Y) aléatoires, issues de cette même liste.

	Méthode « farming » : Permet de modifier l’attribut « collected » de la class « Items » pour chaque objet ayant les mêmes coordonnées que celles de MacGyver. Pour chaque objet avec l’attribut « collected » = « True », l’objet s’effacera du labyrinthe pour s’afficher dans la fenêtre de recensement des objets collectés (fonction présente dans la boucle du jeu).

Victoire ou défaite :

Nous appliquons à la fin de la boucle de jeu une fonction permettant de la finaliser. Si les coordonnées de MacGyver sont identiques à la case « a » de la grille, le jeu s’arrête. Si l’ensemble des objets sont collectés, alors MacGyver a réussi sa mission, à défaut il a échoué.


4. Axes de développement :

Concernant ce projet, plusieurs axes de développement peuvent être opérés. En voici une partie non exhaustive :

Optimiser le code ;
Appliquer des effets sonores via « pygame.mixer » ;
Ajouter un ou plusieurs niveaux au jeu ;
Rendre les objets et le gardien mobile ;
Utiliser le module « rect » pour une plus grande flexibilité des collisions ;
Améliorer les graphismes du jeu, particulièrement MacGyver (sprite de déplacement à droite, gauche, vers le haut, vers le bas par exemple) ;
Améliorer l’ergonomie du jeu ainsi que l’expérience utilisateur.
