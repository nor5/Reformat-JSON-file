import json
import pathlib
from collections import OrderedDict


def extract_ticket_data(json_file):
    # Ouverture du fichier JSON contenant les données des tickets
    with open(json_file, "r") as file:
        # Chargement des données JSON dans une variable
        data = json.load(file)

    # Extraction des éléments de la clé "items" dans la structure de données JSON
    items = data["ordersWithDetails"]["items"]

    # Initialisation de la liste qui contiendra les données des tickets
    ticket_list = []
    # Parcours de chaque élément dans la liste des items
    for item in items:
        # Parcours de chaque commande (order) dans l'élément actuel
        for order in item["orderItems"]:
            # Initialisation d'un dictionnaire pour stocker les attributs de produit modifiés
            modified_attributes = {}
            # Initialisation d'un compteur pour chaque attribut de produit
            counter = {}

            # Récupération des informations du produit de la commande (order)
            infos_products = order["product"]
            # Récupération des options d'attributs du produit de la commande (order)
            productItemAttributeOptions = order["product"][
                "productItemAttributeOptions"
            ]
            # Suppression des options d'attributs du produit de la commande (order)
            infos_products.pop("productItemAttributeOptions")

            # Parcours de chaque option d'attribut du produit
            for option in productItemAttributeOptions:
                # Extraction du code de l'attribut de produit
                attribute_code = option["productAttribute"]["code"]
                # Incrémentation du compteur pour cet attribut de produit
                counter[attribute_code] = counter.get(attribute_code, 0) + 1
                # Création d'un nouveau nom d'attribut en fonction du compteur code d'option
                new_name_attribute = (
                    f"productAttribute_{attribute_code}_{counter[attribute_code]}"
                )
                # Ajout de l'option d'attribut au dictionnaire des attributs modifiés
                modified_attributes[new_name_attribute] = option

            # Parcours de chaque ticket dans la commande (order)
            for ticket in order["tickets"]:
                # Initialisation d'un OrderedDict pour stocker les données du ticket dans un ordre spécifique
                ticket_dict = OrderedDict()
                # Ajout des informations générales de la commande (item) aux données du ticket
                ticket_dict["infos"] = dict(list(item.items())[0:10])
                # Ajout des informations de l'utilisateur associé à la commande aux données du ticket
                ticket_dict["user"] = item["user"]
                # Ajout des informations du canal de vente associé à la commande aux données du ticket
                ticket_dict["salesChannel"] = item["salesChannel"]
                # Ajout des informations spécifiques à la commande (order) aux données du ticket
                ticket_dict["infos_order"] = dict(list(order.items())[0:6])
                # Ajout des informations du produit associé à la commande aux données du ticket
                ticket_dict["infos_products"] = infos_products
                # Ajout des informations spécifiques au ticket aux données du ticket
                ticket_dict["infos_tickets"] = ticket
                # Ajout des attributs modifiés du produit associé à la commande aux données du ticket
                ticket_dict["productItemAttributeOptions"] = modified_attributes
                # Ajout chaque dictionnaire du ticket à la liste des tickets
                ticket_list.append(ticket_dict)

    # récuperer le nom du fichier d'entrée sans extension
    file_name_without_extension = pathlib.Path(json_file).stem
    # construire le nom du fichier du nouveau fichier à partir du nom de fichier d'entrée
    output_file_name = f"modified_{file_name_without_extension}.json"
    # Écriture des données des tickets dans un nouveau fichier JSON avec une mise en forme indentée
    with open(output_file_name, "w") as json_file:
        json.dump(ticket_list, json_file, indent=2)


if __name__ == "__main__":
    
# Définir le chemin du répertoire où se trouvent les fichiers
    path = "fichiers/"

# Générer une liste de chemins de fichiers en itérant sur tous les
# fichiers dans le répertoire spécifié "path"
# et en filtrant uniquement les fichiers en excluant les répertoires
    list_files = [path + f.name for f in pathlib.Path(path).iterdir() if f.is_file()]
    
    # Itérer sur chaque chemin de fichier dans  list_files
    for file in list_files:
        # Appeler la fonction "extract_ticket_data" pour traiter chaque fichier "file"
        extract_ticket_data(file)
