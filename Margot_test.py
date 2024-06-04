import pandas as pd
from time import time
import csv

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


def algo_B(n):
    """
    Deuxieme algo permettant de trier et sélectionnner le nombre d'objet à mettre dans le sac sans dépasser le poids
    en optimisant l'utilité max
    C'est l'algorithme glouton
    :param n: poids max à mettre dans le sac
    :return:
    """
    # Pour chaque nb_op modifié on à toujours +1 car on fait une opéation
    poids_total = 0
    nb_op = 2

    for key in dico.keys():
        dico[key].append(dico[key][1]/dico[key][0])
        nb_op += 2

    dico_tri = sorted(dico.items(), key=lambda objet:objet[1][2], reverse=True)
    nb_op +=2

    rang = 0
    in_bag = []
    nb_op += 3
    while(poids_total < n and rang < len(dico)):
        if(poids_total+dico_tri[rang][1][0] < n):
            #print("Objet ajouté ==> ", dico_tri[rang])
            in_bag.append(dico_tri[rang])
            poids_total += dico_tri[rang][1][0]
        rang +=1
        nb_op += 7

    print("Le poid du sac est : ", poids_total)
    print("Les objets dans le sac sont : ", in_bag)
    print("Le nombre d'opérations maximale est :", nb_op)
    print("Le temps maximal estimé pour cet algo est ", nb_op*1e-7)


