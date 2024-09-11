import json

limit = 10

# batteries de marque X
def afficher_batteries_par_marque(nom_marque):
    # Charger les données JSON depuis le fichier
    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    if "_" in nom_marque:
        nom_marque = nom_marque.replace("_"," / ")

    # Rechercher les batteries de la marque spécifiée
    batteries_marque = [batterie for batterie in donnees if batterie['Marque'] == nom_marque]

    return batteries_marque[:10]

# Appeler la fonction pour afficher les 5 premières batteries de marque "Samsung"
#afficher_batteries_par_marque_et_limite("Samsung", 5)

#Information sur la batterie de référence X

def obtenir_informations_batterie(reference):
    reference = str(reference)[:-2]

    # Charger les données JSON depuis le fichier

    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Rechercher la batterie avec la référence spécifiée
    batterie_recherchee = None
    for batterie in donnees:
        if batterie['_id'] == reference:
            batterie_recherchee = batterie
            break

    if batterie_recherchee:
        informations_batterie = {
            "Référence": batterie_recherchee['_id'],
            "Poids":batterie_recherchee['Poids - g'],
            "Marque": batterie_recherchee['Marque'],
            "Capacité": batterie_recherchee['Capacité typ. - mAh'],
            "Tension": batterie_recherchee['Tension nominale']
        }
        return informations_batterie
    else:
        return None

# Appeler la fonction pour obtenir les informations sur la batterie avec la référence "X"
# informations = obtenir_informations_batterie("7417940526645")

#if informations:
#    print("Informations sur la batterie de référence", informations['Référence'], ":")
#    print("Poids:", informations['Poids'])
#   print("Marque:", informations['Marque'])
#   print("Capacité:", informations['Capacité'])
#    print("Tension:", informations['Tension'])
#else:
#    print("Batterie non trouvée.")

#Quelles sont les différentes marques de batteries?

def lister_marques_de_batteries():
    # Charger les données JSON depuis le fichier
    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Extraire les marques uniques
    marques = set(batterie['Marque'] for batterie in donnees)

    return list(marques)

# Appeler la fonction pour obtenir la liste des marques de batteries
# marques_de_batteries = lister_marques_de_batteries()

#print("Différentes marques de batteries :")
#for marque in marques_de_batteries:
#    print(marque)
   

# la liste des batteries avec la tension inférieure à Y


def batteries_avec_tension_inferieure(tension_seuil):
    tension_seuil = int(tension_seuil)

    # Charger les données JSON depuis le fichier
    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Rechercher les batteries avec une tension inférieure à la valeur seuil
    batteries_tension_inferieure = [batterie for batterie in donnees if float(batterie['Tension nominale'][:-1]) < tension_seuil]

    return batteries_tension_inferieure[:limit]

# Appeler la fonction pour trouver les batteries avec une tension inférieure à 3.7V (par exemple)
# tension_seuil = 3.7
# batteries_inferieures = batteries_avec_tension_inferieure(tension_seuil)

#print("Batteries avec une tension inférieure à", tension_seuil, "V :")
#for batterie in batteries_inferieures:
 #   print(batterie)


#Liste des accumulateurs avec une tension supérieure à Y


def batteries_avec_tension_superieure(tension_seuil):
    tension_seuil = int(tension_seuil)

    # Charger les données JSON depuis le fichier
    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Rechercher les accumulateurs avec une tension supérieure à la valeur seuil
    accumulateurs_tension_superieure = [accumulateur for accumulateur in donnees if float(accumulateur['Tension nominale'][:-1]) > tension_seuil]

    return accumulateurs_tension_superieure[:limit]

# Appeler la fonction pour obtenir la liste des accumulateurs avec une tension supérieure à 3.7V (par exemple)
# tension_seuil = 3.7
# accumulateurs_superieurs = batteries_avec_tension_superieure(tension_seuil)

#if accumulateurs_superieurs!=[]:
 #   print("Liste des accumulateurs avec une tension supérieure à", tension_seuil, "V :")
 #   for accumulateur in accumulateurs_superieurs:
 #       print(accumulateur)

# les batteries avec une tension comprise entre X et Y

def batteries_avec_tension_comprise(tension_min, tension_max):
    tension_min, tension_max = int(tension_min), int(tension_max)
    # Charger les données JSON depuis le fichier
    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Rechercher les batteries avec une tension comprise entre les valeurs minimale et maximale
    batteries_tension_comprise = [
        batterie for batterie in donnees
        if tension_min <= float(batterie['Tension nominale'][:-1]) <= tension_max
    ]

    return batteries_tension_comprise[:limit]

# Appeler la fonction pour trouver les batteries avec une tension comprise entre 3.5V (inférieure) et 3.7V (supérieure)
# tension_min = 2.5
# tension_max = 3.6
# batteries_comprises = batteries_avec_tension_comprise(tension_min, tension_max)

#print("Batteries avec une tension comprise entre", tension_min, "V et", tension_max, "V :")
#for batterie in batteries_comprises:
#    print(batterie)

#les batteries qui ont un poids supérieur à Y

def batteries_avec_tension_minimal():
    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Initialiser la batterie avec le poids minimal comme la première batterie dans les données
    batterie_minimale = donnees[0]

    # Parcourir les données pour trouver la batterie avec le poids minimal
    for batterie in donnees:
        tension_batterie = float(batterie['Tension nominale'][:-1])
        tension_minimale = float(batterie_minimale['Tension nominale'][:-1])
        if tension_batterie < tension_minimale:
            batterie_minimale = batterie

    return batterie_minimale

def batteries_avec_tension_maximal():
    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Initialiser la batterie avec le poids minimal comme la première batterie dans les données
    batterie_maximal = donnees[0]

    # Parcourir les données pour trouver la batterie avec le poids minimal
    for batterie in donnees:
        tension_batterie = float(batterie['Tension nominale'][:-1])
        tension_minimale = float(batterie_maximal['Tension nominale'][:-1])
        if tension_batterie > tension_minimale:
            batterie_maximal = batterie

    return batterie_maximal

def batteries_avec_poids_superieur(poids_seuil):
    poids_seuil = int(poids_seuil)

    # Charger les données JSON depuis le fichier
    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Rechercher les batteries avec un poids supérieur à la valeur seuil
    batteries_poids_superieur = [batterie for batterie in donnees if float(batterie['Poids - g'][:-6]) > poids_seuil]

    return batteries_poids_superieur[:limit]

# Appeler la fonction pour trouver les batteries avec un poids supérieur à 150 grammes (par exemple)
# poids_seuil = 82.0000
# batteries_superieures = batteries_avec_poids_superieur(poids_seuil)

#print("Batteries avec un poids supérieur à", poids_seuil, "grammes :")
#for batterie in batteries_superieures:
#    print(batterie)


#les batteries qui ont un poids inférieur à Y

def batteries_avec_poids_inferieur(poids_seuil):
    poids_seuil = int(poids_seuil)

    # Charger les données JSON depuis le fichier
    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Rechercher les batteries avec un poids inférieur à la valeur seuil
    batteries_poids_inferieur = [batterie for batterie in donnees if float(batterie['Poids - g']) < poids_seuil]

    return batteries_poids_inferieur[:limit]

# Appeler la fonction pour trouver les batteries avec un poids inférieur à 25.0000 grammes (par exemple)
# poids_seuil = 25.0000
# batteries_inferieures = batteries_avec_poids_inferieur(poids_seuil)

#print("Batteries avec un poids inférieur à", poids_seuil, "grammes :")
#for batterie in batteries_inferieures:
#    print(batterie)

#les batteries avec un poids compris entre X et Y

def batteries_avec_poids_compris(poids_min, poids_max):
    poids_min, poids_max = int(poids_min), int(poids_max)

    # Charger les données JSON depuis le fichier
    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Rechercher les batteries avec un poids compris entre les valeurs minimale et maximale
    batteries_poids_compris = [
        batterie for batterie in donnees
        if poids_min <= float(batterie['Poids - g']) <= poids_max
    ]

    return batteries_poids_compris[:limit]

# Appeler la fonction pour trouver les batteries avec un poids compris entre 20.0000 grammes (inférieure) et 50.0000 grammes (supérieure)
# poids_min = 20.0000
# poids_max = 50.0000
# batteries_comprises = batteries_avec_poids_compris(poids_min, poids_max)

#print("Batteries avec un poids compris entre", poids_min, "grammes et", poids_max, "grammes :")
#for batterie in batteries_comprises:
#   print(batterie)

#batterie avec Poids minimal

def batterie_avec_poids_minimal():
    # Charger les données JSON depuis le fichier
    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Initialiser la batterie avec le poids minimal comme la première batterie dans les données
    batterie_minimale = donnees[0]

    # Parcourir les données pour trouver la batterie avec le poids minimal
    for batterie in donnees:
        poids_batterie = float(batterie['Poids - g'])
        poids_minimal = float(batterie_minimale['Poids - g'])
        if poids_batterie < poids_minimal:
            batterie_minimale = batterie

    return batterie_minimale

# Appeler la fonction pour trouver la batterie avec le poids minimal
# batterie_minimale = batterie_avec_poids_minimal()

#print("Batterie avec le poids minimal :")
#print(batterie_minimale)


#batterie avec Poids maximal
def batterie_avec_poids_maximal():
    # Charger les données JSON depuis le fichier
    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Initialiser la batterie avec le poids maximal comme la première batterie dans les données
    batterie_maximale = donnees[0]

    # Parcourir les données pour trouver la batterie avec le poids maximal
    for batterie in donnees:
        poids_batterie = float(batterie['Poids - g'])
        poids_maximal = float(batterie_maximale['Poids - g'])
        if poids_batterie > poids_maximal:
            batterie_maximale = batterie

    return batterie_maximale

# Appeler la fonction pour trouver la batterie avec le poids maximal
# batterie_maximale = batterie_avec_poids_maximal()

#print("Batterie avec le poids maximal :")
#print(batterie_maximale)


#batteries avec une capacité inférieure à X

def batteries_avec_capacite_inferieure(capacite_seuil):
    capacite_seuil = int(capacite_seuil)

    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Rechercher les batteries avec une tension inférieure à la valeur seuil
    batteries_capacite_inferieure = [batterie for batterie in donnees if float(batterie['Capacité typ. - mAh']) < capacite_seuil]

    return batteries_capacite_inferieure[:limit]


# Appeler la fonction pour trouver les batteries avec une capacité inférieure à 3 200,00 mAh (par exemple)
# capacite_seuil = "3 200,00"
# batteries_inferieures = batteries_avec_capacite_inferieure(capacite_seuil)

#("Batteries avec une capacité inférieure à", capacite_seuil, "mAh :")
#for batterie in batteries_inferieures:
#    print(batterie)

# batteries capacité supérieure à Y


def batteries_avec_capacite_superieure(capacite_seuil):
    capacite_seuil = int(capacite_seuil)

    # Charger les données JSON depuis le fichier
    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Rechercher les batteries avec une tension inférieure à la valeur seuil
    batteries_capacite_superieur = [batterie for batterie in donnees if float(batterie['Capacité typ. - mAh']) > capacite_seuil]

    return batteries_capacite_superieur[:limit]

# Appeler la fonction pour trouver les batteries avec une capacité inférieure à 3 200,00 mAh (par exemple)
# capacite_seuil = "3 200,00"
# batteries_superieures = batteries_avec_capacite_superieure(capacite_seuil)

#print("Batteries avec une capacité inférieure à", capacite_seuil, "mAh :")
#for batterie in batteries_superieures:
#    print(batterie)

#batteries capacité comprise entre X et Y


def batteries_avec_capacite_comprise(capacite_min, capacite_max):
    capacite_min, capacite_max = float(capacite_min), float(capacite_max)

    # Charger les données JSON depuis le fichier
    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
    
    batteries_capacite_comprise = [
        batterie for batterie in donnees
        if capacite_min <= float(batterie['Capacité typ. - mAh']) <= capacite_max
    ]

    return batteries_capacite_comprise[:limit]

# Appeler la fonction pour trouver les batteries avec une capacité comprise entre 3 000,00 mAh (inférieure) et 4 000,00 mAh (supérieure)
# capacite_min = "3 000,00"
# capacite_max = "4 000,00"
# batteries_comprises = batteries_avec_capacite_comprise(capacite_min, capacite_max)

#print("Batteries avec une capacité comprise entre", capacite_min, "mAh et", capacite_max, "mAh :")
#for batterie in batteries_comprises:
#    print(batterie)

#batterie capacité minimale

def batterie_avec_capacite_minimale():
    # Charger les données JSON depuis le fichier
    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Initialiser la batterie avec la capacité minimale comme la première batterie dans les données
    batterie_minimale = donnees[0]

    # Parcourir les données pour trouver la batterie avec la capacité minimale
    for batterie in donnees:
        capacite_batterie = float(batterie['Capacité typ. - mAh'].replace(" ", "").replace(",", "."))
        capacite_minimale = float(batterie_minimale['Capacité typ. - mAh'].replace(" ", "").replace(",", "."))
        if capacite_batterie < capacite_minimale:
            batterie_minimale = batterie

    return batterie_minimale

# Appeler la fonction pour trouver la batterie avec la capacité minimale
# batterie_minimale = batterie_avec_capacite_minimale()

#print("Batterie avec la capacité minimale :")
#print(batterie_minimale)


#batterie capacité maximale


def batterie_avec_capacite_maximale():
    # Charger les données JSON depuis le fichier
    with open('battery_data.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Initialiser la batterie avec la capacité maximale comme la première batterie dans les données
    batterie_maximale = donnees[0]

    # Parcourir les données pour trouver la batterie avec la capacité maximale
    for batterie in donnees:
        capacite_batterie = float(batterie['Capacité typ. - mAh'].replace(" ", "").replace(",", "."))
        capacite_maximale = float(batterie_maximale['Capacité typ. - mAh'].replace(" ", "").replace(",", "."))
        if capacite_batterie > capacite_maximale:
            batterie_maximale = batterie

    return batterie_maximale

# Appeler la fonction pour trouver la batterie avec la capacité maximale
# batterie_maximale = batterie_avec_capacite_maximale()

#("Batterie avec la capacité maximale :")
#print(batterie_maximale)


function_map_zero_op = {
    'marques_batteries': lister_marques_de_batteries, 
    'tension_minimale': batteries_avec_tension_minimal,
    'tension_maximale': batteries_avec_tension_maximal, 
    'poids_minimal': batterie_avec_poids_minimal, 
    'poids_maximal': batterie_avec_poids_maximal,
    'capacite_maximale': batterie_avec_capacite_maximale, 
    'capacite_minimale': batterie_avec_capacite_minimale
}

function_map_un_op = {
    'information_batterie': obtenir_informations_batterie, 
    'tension_inferieure': batteries_avec_tension_inferieure, 
    'tension_superieure': batteries_avec_tension_superieure, 
    'poids_inferieur': batteries_avec_poids_inferieur, 
    'poids_superieur': batteries_avec_poids_superieur, 
    'capacite_inferieure': batteries_avec_capacite_inferieure,
    'capacite_superieure': batteries_avec_capacite_superieure
}

function_map_deux_op = {
    'tension_intervalle': batteries_avec_tension_comprise, 
    'poids_intervalle': batteries_avec_poids_compris, 
    'capacite_intervalle': batteries_avec_capacite_comprise
}
def get_value(tag, op=[]):
    ret = []

    if "batteries_" in tag:
        return afficher_batteries_par_marque(tag[10:])
    
    if len(op) == 0:
        ret = function_map_zero_op[tag]()
    elif len(op) == 1:
        ret = function_map_un_op[tag](op[0])
    elif len(op) == 2:
        op = [int(o) for o in op]
        ret = function_map_deux_op[tag](op[0], op[1])
    
    if type(ret) != list:
        ret = [ret]

    return ret