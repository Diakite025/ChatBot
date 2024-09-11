import json

def enlever_doublons_par_id(fichier_entree, fichier_sortie):
    # Charger le fichier JSON
    with open(fichier_entree, 'r', encoding='utf-8') as fichier:
        data = json.load(fichier)

    # Créer un dictionnaire pour stocker les objets uniques en utilisant la clé "_id"
    objets_uniques = {}
    for objet in data:
        objet_id = objet.get("_id")
        if objet_id not in objets_uniques:
            objets_uniques[objet_id] = objet

    # Convertir le dictionnaire en une liste d'objets uniques
    objets_uniques = list(objets_uniques.values())

    # Écrire les objets uniques dans un nouveau fichier JSON avec l'encodage UTF-8
    with open(fichier_sortie, 'w', encoding='utf-8') as fichier_sortie:
        json.dump(objets_uniques, fichier_sortie, ensure_ascii=False, indent=4)

    print("Doublons basés sur la clé '_id' ont été supprimés, le fichier a été enregistré dans", fichier_sortie)

# Utilisation de la fonction pour enlever les doublons par '_id'
# enlever_doublons_par_id('battery_data.json', 'nouveau_fichier.json')

def reformat_string_to_correct_float(fichier_entree,fichier_sortie):
    with open(fichier_entree, 'r', encoding='utf-8') as fichier:
        data = json.load(fichier)
    
    for objet in data:
        objet["Min. capacité - mAh"] = objet.get("Min. capacité - mAh").replace(",",".")
        objet["Min. capacité - mAh"] = objet.get("Min. capacité - mAh").replace(" ","")
        objet["Capacité typ. - mAh"] = objet.get("Capacité typ. - mAh").replace(",",".")
        objet["Capacité typ. - mAh"] = objet.get("Capacité typ. - mAh").replace(" ","")

    with open(fichier_sortie, 'w', encoding='utf-8') as fichier_sortie:
        json.dump(data, fichier_sortie, ensure_ascii=False, indent=4)

reformat_string_to_correct_float('battery_data.json','battery_data.json')
