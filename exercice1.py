import numpy as np
import csv
from time import time


dico = {
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

#=============== FONCTIONS ==================
def question1_2():
    n_objets = [1, 2, 10, 23]
    print("Question 1 :")
    for i in n_objets:
        print("Nombre de possibilités pour", i, "objets:", 2**i)
    print("\nQuestion2 :\nNombre max de possibilités :", 2**max(n_objets))


# Question 3 :
# Utilité maximale pour un poids inférieur ou égal à 0.6 : 7.6 avec 6 objets pour un poids total de 0.6

def question5(n):
    start = time()
    # Il faut varier l'opération et le n pour tester les différentes opérations
    for i in range(n):
        op = 36 / 39
    stop = time()

    print("Le temps est d'environ: ",stop-start)

def bruteforce(poids_max):
    """
    Algorithme de recherche exacte trèèèèèèèèèèèèèèèès lent
    :param poids_max:
    :return:
    """
    poidsmax = 0
    utilitemax = 0
    objetmax = []
    start = time()
    for i in range(2**len(dico)):
        poids = 0
        utilite = 0
        objet = []
        for j in range(len(dico)):
            #if i & 1 << j:
            poids += dico[list(dico.keys())[j]][0]
            utilite += dico[list(dico.keys())[j]][1]
            objet.append(list(dico.keys())[j])
        if poids <= poids_max and utilite > utilitemax:
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


def recherche_locale(poids_max):
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
        dico[key].append(dico[key][1] / dico[key][0])
        nb_op += 1
    dico2 = dico.copy()
    nb_op += 1
    while poidsmax < poids_max:
        ratiomax = 0
        for i in dico2.keys():
            if dico2[i][2] > ratiomax:
                ratiomax = dico2[i][2]
                rangmax = i
                nb_op += 2
            nb_op += 1
        objetmax.append(dico2[rangmax])
        poidsmax += dico2[rangmax][0]
        dico2.pop(rangmax)
        nb_op += 3
    print(objetmax)
    print("Temps estimé pour cet algo :", nb_op*1e-7, "secondes")

def algo_B(n):
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
        dico[key].append(dico[key][1]/dico[key][0])
        nb_op += 2

    dico_tri = sorted(dico.items(), key=lambda objet:objet[1][2], reverse=True)
    nb_op += 2

    rang = 0
    in_bag = []
    nb_op += 3
    while poids_total < n and rang < len(dico):
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
