import time
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

def question6(poids_max):
    poidsmax = 0
    utilitemax = 0
    objetmax = []
    start = time.time()
    for i in range(2**len(dico)):
        poids = 0
        utilite = 0
        objet = []
        for j in range(len(dico)):
            if i & 1 << j:
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

def algo_B(poids_max):
    poids = 0
    nb_objets = 0
    utilite = 0
    while poids < poids_max:
        objets = sorted(dico.items(), key=lambda x: x[1][1]/x[1][0], reverse=True)
        for objet in objets:
            if poids + objet[1][0] <= poids_max:
                poids += objet[1][0]
                utilite += objet[1][1]
                nb_objets += 1

#https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos