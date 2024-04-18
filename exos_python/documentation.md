## Explication du script "testSolution":

"testSolution.py" est un script écrit en python V3.9. Son objectif est de formater les données des tickets à partir d'un ensemble de fichiers JSON contenant des données de commandes.

### Importation des Modules :
        Le script commence par l'importation des modules nécessaires :
            json : Pour travailler avec des données JSON.
            pathlib : Pour manipuler les chemins de fichiers de manière plus propre et portable.
            OrderedDict : Pour créer un dictionnaire ordonné qui préserve l'ordre des éléments tels qu'ils sont insérés.

### Définition de la Fonction extract_ticket_data :
        Cette fonction prend en argument le chemin d'un fichier JSON contenant des données de commandes.
        Elle ouvre le fichier JSON spécifié, charge les données JSON dans une variable, puis commence à extraire et traiter les données de tickets.

### Extraction des Données de Tickets :
        La fonction parcourt chaque élément dans la liste des articles de la commande (items).
        Pour chaque article de commande, elle parcourt chaque commande (order) dans cet élément.
        Pour chaque commande, elle récupère les informations sur le produit de la commande et ses options d'attributs.
        Elle crée un nouveau nom pour chaque attribut en fonction de son code et de son compteur, puis stocke les options d'attributs modifiées dans un dictionnaire.
        Pour chaque ticket dans la commande, elle crée un dictionnaire ordonné contenant les informations générales de la commande, de l'utilisateur, du canal de vente, de la commande elle-même, du produit associé, du ticket et des attributs modifiés du produit.
        Elle ajoute ensuite ce dictionnaire de ticket à une liste qui contient toutes les données de tickets traitées.

### Écriture des Données de Tickets dans un Nouveau Fichier JSON :
        Une fois toutes les données de tickets traitées et stockées dans la liste ticket_list, la fonction récupère le nom du fichier d'entrée sans extension à l'aide de pathlib.Path(json_file).stem.
        Elle construit ensuite le nom du fichier de sortie en ajoutant le préfixe "modified_" au nom du fichier d'entrée.
        Enfin, elle écrit les données de tickets dans un nouveau fichier JSON avec une mise en forme indentée, en utilisant le nom de fichier de sortie construit précédemment.

### Exécution du Traitement sur un Ensemble de Fichiers :
        Dans la section if __name__ == "__main__":, le script commence par définir le chemin du répertoire où se trouvent les fichiers à traiter.
        Il génère ensuite une liste de chemins de fichiers en itérant sur tous les fichiers dans le répertoire spécifié et en filtrant uniquement les fichiers (en excluant les répertoires).
        Enfin, il itère sur chaque chemin de fichier dans cette liste et appelle la fonction extract_ticket_data pour traiter chaque fichier individuellement.