from time import time
import math
import random
import numpy as np


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

def question10(poids_max):
    poidsmax = 0
    utilitemax = 0
    objetmax = []
    start = time.time()
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
    end = time.time()
    print("Utilité maximale pour un poids inférieur ou égal à ", poids_max, " :", utilitemax, "avec", len(objetmax), "objets pour un poids total de", poidsmax)
    print("Objets choisis :", objetmax)
    print("Temps d'exécution :", end-start)

'''
    Nb d'opérations pour l'algo bruteforce : 3+2**23*(8+23*4)  = 838860803
    temps d'exécution d'une opération : 1e-7
    temps d'exécution total : 83.8860803 secondes
'''

def recherche_locale(poids_max):
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


def online3(dico):
    """
    Rangement en ne prenant en compte toutes les dimensions (longueur, largeur, hauteur) des marchandises et on ne peut
    pas les trier au départ.
    :param dico:
    :return:
    """
    merch = dico.copy()
    wagon = []
    dimensions_wagon = [11.583, 2.294]
    shelf = []
    train = []
    shelf_size = [11.583, 0]
    for item in merch.keys():
        if not train:
            if not wagon:
                if not shelf:
                    shelf.append(item)
                    if shelf_size[1] < merch[item][1]:
                        shelf_size[1] = merch[item][1]
                    print("aaaaa")
                else:
                    if shelf_size[0] >= merch[item][0]:
                        shelf.append(item)
                        shelf_size[0] -= merch[item][0]
                        if shelf_size[1] < merch[item][1]:
                            shelf_size[1] = merch[item][1]
                        print("bbbbb")
                    else:
                        wagon.append(shelf)
                        dimensions_wagon[1] -= shelf_size[1]
                        shelf = [item]
                        shelf_size[0] = dimensions_wagon[0] - merch[item][0]
                        shelf_size[1] = 0
                        print("ccccc")
            else:
                if dimensions_wagon[1] >= shelf_size[1]:
                    wagon.append(shelf)
                    dimensions_wagon[1] -= shelf_size[1]
                    print("eeeee")
                else:
                    train.append(wagon)
                    wagon = [shelf]
                    dimensions_wagon[1] = 2.294 - shelf_size[1]
                    print("fffff")
    print(train)
    print(len(train))