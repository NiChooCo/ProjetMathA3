import numpy as np
import csv
from time import time


# =============== VARIABLES ================

# Dictionnaire des objets avec leur poids et utilité
dico_objet = {
    "Pompe": [0.2, 1.5],
    "Démonte-pneus": [0.1, 1.5],
    "Gourde": [1, 2],
    "Chambre à air": [0.2, 0.5],
    "Clé de 15": [0.3, 1],
    "Multi-tool": [0.2, 1.7],
    "Pince multiprise": [0.4, 0.8],
    "Couteau suisse": [0.2, 1.5],
    "Compresses": [0.1, 0.4],
    "Désinfectant": [0.2, 0.6],
    "Veste de pluie": [0.4, 1],
    "Pantalon de pluie": [0.4, 0.75],
    "Crème solaire": [0.4, 1.75],
    "Carte IGN": [0.1, 0.2],
    "Batterie Portable": [0.5, 0.4],
    "Téléphone mobile": [0.4, 2],
    "Lampes": [0.3, 1.8],
    "Arrache Manivelle": [0.4, 0],
    "Bouchon valve chromé bleu": [0.01, 0.1],
    "Maillon rapide": [0.05, 1.4],
    "Barre de céréales": [0.4, 0.8],
    "Fruits": [0.6, 1.3],
    "Rustines": [0.05, 1.5]
}


# Dictionnaire des objets avec uniquement leur poids
dico_exact = {
    "Pompe": 0.2,
    "Démonte-pneus": 0.1,
    "Gourde": 1,
    "Chambre à air": 0.2,
    "Clé de 15": 0.3,
    "Multi-tool": 0.2,
    "Pince multiprise": 0.4,
    "Couteau suisse": 0.2,
    "Compresses": 0.1,
    "Désinfectant": 0.2,
    "Veste de pluie": 0.4,
    "Pantalon de pluie": 0.4,
    "Crème solaire": 0.4,
    "Carte IGN": 0.1,
    "Batterie Portable": 0.5,
    "Téléphone mobile": 0.4,
    "Lampes": 0.3,
    "Arrache Manivelle": 0.4,
    "Bouchon valve chromé bleu": 0.01,
    "Maillon rapide": 0.05,
    "Barre de céréales": 0.4,
    "Fruits": 0.6,
    "Rustines": 0.05
}


# =============== FONCTIONS ==================


def question1_2(n_objets):
    """
    Fonction permettant de répondre aux questions 1 et 2 réalisée par Nicolas
    :param n_objets:
    :return:
    """
    print("Question 1 :")
    for i in n_objets:
        print("Nombre de possibilités pour", i, "objets:", 2**i)
    print("\nQuestion2 :\nNombre max de possibilités :", 2**max(n_objets))


# --------------------------------------------


# Question 3 : (réalisé par Margot et Emir)
# Utilité maximale pour un poids inférieur ou égal à 0.6 : 7.6 avec 6 objets pour un poids total de 0.6


# --------------------------------------------

# Question 5

def question5(n):
    """
    Réalisée par Nicolas et Margot
    Fonction permettant de calculer le temps pour un nombre n d'opérations
    :param n: le nombre d'opérations à réaliser
    :return:
    """
    start = time()
    # Il faut varier l'opération et le n pour tester les différentes opérations
    for i in range(n):
        op = 36 / 39
    stop = time()

    print("Le temps réel est d'environ: ", stop-start)
    print("Le temps estimé est de : ", n*1e-7) # Temps estimé d'une opération : 1e-7s


# --------------------------------------------


# Question 6 (Réalisé par Emir, Margot et Nicolas)

# Il faut tester
    # temps = nombre d'opérations * temps d'une opération
    # temps = (2**23) * (1e-7)
    # temps = 0.8388608 secondes


# --------------------------------------------


# Question 8 (Réalisé par Nicolas)

def bruteforce(poids_max, dico):
    """
    Algorithme de recherche exacte très lent qui teste toutes les possibilités et retourne la meilleure
    :param poids_max: Poids maximal que peut porter le sac
    :return:
    """
    poidsmax = 0
    utilitemax = 0
    objetmax = []
    start = time()
    for i in range(2**len(dico)): # Permet de tester toutes les combinaisons possibles
        poids = 0
        utilite = 0
        objet = []
        for j in range(len(dico)):
            if i & 1 << j:  # Permet de vérifier si l'objet est dans le sac via les bits de i (si le bit de l'bjet dans
                # i est = 1 alors l'objet est dans le sac)
                # Exemple : i = 5 = 101 en binaire, donc les objets 1 et 3 sont dans le sac, ça permet de ne
                # pas vérifier les objets qui ne sont pas dans le sac et don cde gagner du temps
                poids += dico[list(dico.keys())[j]][0]
                utilite += dico[list(dico.keys())[j]][1]
                objet.append(list(dico.keys())[j])
        if poids <= poids_max and utilite > utilitemax:  # teste si le poids de la combinaison est inférieur ou égal au
            # poids max et si l'utilité de cette combinaison est supérieure à l'utilité max
            # Auquel cas on met à jour les valeurs maximales
            poidsmax = poids
            utilitemax = utilite
            objetmax = objet
    end = time()
    print("Utilité maximale pour un poids inférieur ou égal à ", poids_max, " :", utilitemax, "avec", len(objetmax), "objets pour un poids total de", poidsmax)
    print("Objets choisis :", objetmax)
    print("Temps d'exécution :", end-start)


'''
    Nb d'opérations pour l'algo bruteforce : 3+2**23*(8+23*4)  = 838860803
    temps d'exécution d'une opération : 1e-7
    temps d'exécution total : 83.8860803 secondes
'''

# Autre solution plus rapide (Réalisé par Emir)

def tree(dico, max_weight=0.6, current_weight=0, current_subset=set()):
    """
    Algorithme exact créé par Emir
    Méthode récursive qui teste toutes les possiblités sous format d'arbre binaire
    :param dico: dictionaire avec tous les objets que l'on peut mettre dans le sac
    :param max_weight: poids maximal que peut porter le sac
    :param current_weight: poids actuel du sac
    :param current_subset: liste des objets présents dans le sac
    :return:
    """
    # Initialisation de la méthode yield
    if len(dico) == 0:
        yield current_subset, current_weight
        return

    # Prendre le premier élément et poids du dictionnaire
    first_element, first_weight = next(iter(dico.items()))

    # Prendre le reste du dictonnaire
    rest_dico = {k: dico[k] for k in dico if k != first_element}

    # Appel récursif pour le reste du dictionnaire
    for subset, weight in tree(rest_dico, max_weight, current_weight, current_subset):
        # Retourne le sous-ensemble et le poids sans ajouter le premier élément
        if weight <= max_weight:
            yield subset, weight
        # Retourne le sous-ensemble et le poids en ajoutant premier élément
        if weight + first_weight <= max_weight:
            yield subset.union({first_element}), weight + first_weight


# --------------------------------------------


# Question 11 et 12 (Réalisé par Margot et Nicolas)

def recherche_locale(poids_max, dico):
    """
    Méthode approchée plus "lente" que l'algorithme glouton
    :param poids_max:
    :return:
    """
    rangmax = 0
    objetmax = []
    poidsmax = 0
    nb_op = 3
    for key in dico.keys():
        dico[key].append(dico[key][1] / dico[key][0])  # Ajout du ratio utilité/poids au dictionnaire
        nb_op += 1
    dico2 = dico.copy() # Copie du dictionnaire pour ne pas le modifier
    nb_op += 1
    while poidsmax < poids_max:
        ratiomax = 0
        for i in dico2.keys():
            if dico2[i][2] > ratiomax:  # Recherche de l'objet avec le meilleur ratio
                ratiomax = dico2[i][2]
                rangmax = i
                nb_op += 2
            nb_op += 1
        objetmax.append(dico2[rangmax])  # Ajout de l'objet avec le meilleur ratio dans le sac
        poidsmax += dico2[rangmax][0]
        dico2.pop(rangmax)
        nb_op += 3
    print(objetmax)
    print("Temps estimé pour cet algo :", nb_op*1e-7, "secondes")


# --------------------------------------------


# Question 13 (Réalisé par Margot, Emir et Nicolas)

# L'algorithme B est plus rapide que l'algorithme A car il ne teste pas toutes les possibilités mais trie les objets
# en revanche l'algorithme A est plus précis


# --------------------------------------------


# Question 14 (Réalisé par Margot)

def algo_B(n, dico):
    """
    Deuxieme algo permettant de trier et sélectionnner le nombre d'objet à mettre dans le sac sans dépasser le poids
    en optimisant l'utilité max
    C'est l'algorithme glouton
    :param n: poids max à mettre dans le sac
    :return:
    """
    # Pour chaque nb_op modifié on à toujours +1 car on fait une opéation
    nb_op = 1
    poids_total = 0
    nb_op += 2

    for key in dico.keys():
        dico[key].append(dico[key][1]/dico[key][0]) # Ajout du ratio utilité/poids au dictionnaire
        nb_op += 2

    dico_tri = sorted(dico.items(), key=lambda objet:objet[1][2], reverse=True) # Tri des objets par ratio
    nb_op += 2

    rang = 0
    in_bag = []
    nb_op += 3
    while poids_total < n and rang < len(dico): # Ajoute les objets dans le sac tant que le poids total est inférieur
        # au poids maximal
        if poids_total+dico_tri[rang][1][0] < n:
            # print("Objet ajouté ==> ", dico_tri[rang])
            in_bag.append(dico_tri[rang])
            poids_total += dico_tri[rang][1][0]
        rang += 1
        nb_op += 7

    print("Le poids du sac est : ", poids_total)
    print("Les objets dans le sac sont : ", in_bag)
    print("Le nombre d'opérations maximale est :", nb_op)
    print("Le temps maximal estimé pour cet algo est ", nb_op*1e-7)
