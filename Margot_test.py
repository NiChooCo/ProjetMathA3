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


# ====================== TEST 2D ======================


def online2(dico):
    """
    Rangement en ne prenant en compte que la longueur et la largeur des marchandises et on ne peut pas les trier au départ.
    :param dico:
    :return:
    """
    train = []
    longueur_wagon = 11.583
    largeur_wagon = 2.294

    largeur_max = 0
    largeur_ecart = 0

    for item in dico.keys():

        if not train:
            train.append([item, dico[item]])
            print(train)

        else:
            for w in train:
                longueurW = 0
                largeur_max = 0

                if len(w) == 2:
                    for l in w:
                        longueurW += float(l[1][0])
                    for i in range(len(w)):
                        if (longueurW + dico[item][0] <= longueur_wagon):
                            w.append([item, dico[item]])
                            if (dico[item][1] > largeur_max):
                                largeur_max = float(dico[item][1])


                        elif (largeur_wagon - largeur_max <= dico[item][1]):
                            w.append([item, dico[item]])
                        print("Le wagon modif", w)

                else:
                    print(len(w))
                    longueurW = w[1][0]
                    if (longueurW + dico[item][0] <= longueur_wagon):
                        w.append([item, dico[item]])
                        if (dico[item][1] > largeur_max):
                            largeur_max = dico[item][1]

                    elif (largeur_wagon - largeur_max <= dico[item][1]):
                        w.append([item, dico[item]])

    print("On a", len(train), "wagons pour mettre tous les objets dans le train.")