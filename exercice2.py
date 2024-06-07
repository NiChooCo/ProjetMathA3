import pandas as pd
import math
from matplotlib import pyplot as plt
import random
from time import time


def create_dico(datapath):
    """
    Fonction réalisée par Margot
    Créer un dictionnaire avec les données du csv
    :param datapath: chemin vers le fichier csv
    :return: un dictionnaire
    """
    data = pd.read_csv(datapath, header=0, delimiter=";")
    new = {}

    for i in range(len(data)):
        # Vérification que le nom n'est pas dans les clés du nouveau dictionnaire pour éviter de modifier les données
        # déjà existantes
        if (data["Désignation"][i] in new.keys()):
            new_name = data["Désignation"][i] + str(i)
            new[new_name] = [data["Longueur"][i], data["Largeur"][i], data["Hauteur"][i]]
        else:
            new[data["Désignation"][i]] = [data["Longueur"][i], data["Largeur"][i], data["Hauteur"][i]]

    # print(new)
    return (new)


# ================ Algorithmes offlines =====================
# First Fit decreasing

def online1(dico):
    """
    Fonction réalisée par Nicolas assisté par Margot
    Rangement en ne prenant en compte que la longueur des marchandises et on ne peut pas les trier au départ.
    :param dico: Un dictionnaire comportant tous les objets à mettre dans le train
    :return: Une liste de liste qui correspond au train et aux wagons remplis
    """
    # Données de base
    train = []
    longueur_wagon = 11.583
    tab_longueur = []
    dimension_totale = 0

    for item in dico.keys():
        # Vérification que le train comporte un wagon
        if not train:
            tab_longueur.append(longueur_wagon - float(dico[item][0]))
            dimension_totale += float(dico[item][0])
            train.append(dico[item])
        else:
            for i in range(len(train)):
                if tab_longueur[i] >= float(dico[item][0]):
                    tab_longueur[i] -= float(dico[item][0])
                    dimension_totale += float(dico[item][0])
                    train[i].append(item)
                    break
            else:
                tab_longueur.append(longueur_wagon - float(dico[item][0]))
                dimension_totale += float(dico[item][0])
                train.append([item])

    #print(train)
    #print(tab_longueur)
    print("Dimensions non utilisées :", len(train) * longueur_wagon - dimension_totale, "mètres")
    print("On a", len(train), "wagons pour mettre tous les objets dans le train.")

    return train


def online2(dico):
    """
    Fonction réalisée par Margot, elle n'est pas opérationnelle
    Rangement en ne prenant en compte que la longueur et la largeur des marchandises et on ne peut pas les trier au
    départ.
    :param dico: Un dictionnaire comportant tous les objets à mettre dans le train
    :return: Une liste de liste qui correspond au train et aux wagons remplis
    """
    train = []
    longueur_wagon = 11.583
    largeur_wagon = 2.294

    dico2 = dico.copy()

    largeur_max = 0
    largeur_ecart = 0
    longueur_r = 0

    tab_longueur = []
    tab_largeur = []

    for item in dico2.keys():
        if not train:
            tab_longueur.append(longueur_wagon - float(dico2[item][0]))
            tab_largeur.append(largeur_wagon - float(dico2[item][1]))
            train.append([item, dico[item]])
        else:
            for i in range(len(train)):
                # Vérification que les dimensions de l'objet rentrent dans le wagon
                if tab_longueur[i] > float(dico2[item][0]):
                    tab_longueur[i] -= float(dico2[item][0])
                    train[i].append([item, dico[item]])
                    # dico2.pop(item)
                    break

                elif tab_largeur[i] > float(dico2[item][1]):
                    tab_largeur[i] -= float(dico2[item][1])
                    train[i].append([item, dico[item]])
                    tab_longueur[i] = longueur_wagon - float(dico2[item][0])
                    # dico2.pop(item)
                    break

                # print("Train à l'étape", i , "==<>",train[i])
            else:
                tab_longueur.append(longueur_wagon - float(dico2[item][0]))
                tab_largeur.append(largeur_wagon - float(dico2[item][1]))
                train.append([item, dico[item]])

    #print(train)
    print("On a", len(train), "wagons pour mettre tous les objets dans le train.")
    return train

def volume_libre_2d(wagon):
    longueur_wagon = round(11.583/0.1)
    largeur_wagon = round(2.294/0.1)

    volume = sum(sum(1 for y in range(largeur_wagon) if wagon["espace"][x][y] == 0) for x in range(longueur_wagon))
    return volume * 0.1 * 0.1

def online2_emir(dico):
    """
    Fonction réalisée par Emir
    Rangement en ne prenant en compte que la longueur et la largeur des marchandises et on ne peut pas les trier au départ.
    :param dico: Un dictionnaire comportant tous les objets à mettre dans le train
    :return: Une liste de liste qui correspond au train et aux wagons remplis
    """
    # Dimension du wagon en multiple 0.1
    longueur_wagon = round(11.583 / 0.1)
    largeur_wagon = round(2.294 / 0.1)

    def creer_wagon():
        """
        Création d'un wagon vide
        :return: Un wagon vide, un dictionnaire avec l'espace du wagon sous forme de matrice et les informations des
        objets présents
        """
        return {
            "espace": [[0] * largeur_wagon for w in range(longueur_wagon)],
            "items": []
        }

    # Initialisation du train avec le premier wagon
    train = []
    wagon = creer_wagon()
    train.append(wagon)

    def placer_objet(wagon, longueur_objet, largeur_objet, nom_objet):
        """
        Placer un objet dans le wagon
        :param wagon: Le wagon (une matrice) dans lequel on veut mettre l'objet
        :param longueur_objet: La longueur de l'objet à ajouter
        :param largeur_objet: La largeur de l'objet à ajouter
        :param nom_objet: La désignation de l'objet
        :return: True si réussi sinon False
        """
        # Parcours du wagon entier où l'objet pourrait être placé sans dépasser ses dimensions
        for i in range(longueur_wagon - longueur_objet + 1):
            for j in range(largeur_wagon - largeur_objet + 1):
                # Vérification de l'espace libre pour l'objet
                if all(wagon["espace"][i + x][j + y] == 0 for x in range(longueur_objet) for y in range(largeur_objet)):
                    # Mise en place de l'objet dans le wagon
                    for x in range(longueur_objet):
                        for y in range(largeur_objet):
                            wagon["espace"][i + x][j + y] = 1
                    wagon["items"].append(nom_objet)
                    return True
        return False

    # Recherche les dimensions des objets dans le dictionnaire
    for item in dico.keys():
        longueur_objet = round(float(dico[item][0]) / 0.1)
        largeur_objet = round(float(dico[item][1]) / 0.1)

        # Placer l'objet dans chaque wagon existant
        for wagon in train:
            if placer_objet(wagon, longueur_objet, largeur_objet, item):
                break
        else:
            # Création d'un nouveau wagon si l'objet ne peut pas être placé dans les wagons existants
            new_wagon = creer_wagon()
            train.append(new_wagon)
            if not placer_objet(new_wagon, longueur_objet, largeur_objet, item):
                break

    print("On a", len(train), "wagons pour mettre tous les objets dans le train.")
    return train


def volume_libre_3d(wagon):
    longueur_wagon = round(11.583/0.1)
    largeur_wagon = round(2.294/0.1)
    hauteur_wagon = round(2.569/0.1)

    volume = sum(sum(sum(1 for z in range(hauteur_wagon)
                         if wagon["espace"][x][y][z] == 0)
                     for y in range(largeur_wagon))
                 for x in range(longueur_wagon))
    return volume * 0.1 * 0.1 * 0.1

def online3(dico):
    """
    Fonction réalisé par Emir et assisté de Margot
    Rangement en ne prenant en compte toutes les dimensions (longueur, largeur, hauteur) des marchandises et on ne peut
    pas les trier au départ.
    :param dico: Un dictionnaire comportant tous les objets à mettre dans le train
    :return: Une liste de liste qui correspond au train et aux wagons remplis
    """
    # Dimension du wagon en multiple 0.1
    longueur_wagon = round(11.583 / 0.1)
    largeur_wagon = round(2.294 / 0.1)
    hauteur_wagon = round(2.569 / 0.1)

    def creer_wagon():
        """
        Création d'un wagon vide
        :return: Un wagon vide, un dictionnaire avec l'espace du wagon sous forme de matrice et les informations des
            objets présents
        """
        return {
            "espace": [[[0] * hauteur_wagon for w in range(largeur_wagon)] for w in range(longueur_wagon)],
            "items": []
        }

    # Initialisation du train avec le premier wagon
    train = []
    wagon = creer_wagon()
    train.append(wagon)

    def placer_objet(wagon, longueur_objet, largeur_objet, hauteur_objet, nom_objet):
        """
        Placer un objet dans le wagon
        :param wagon: Le wagon (une matrice) dans lequel on veut mettre l'objet
        :param longueur_objet: La longueur de l'objet à ajouter
        :param largeur_objet: La largeur de l'objet à ajouter
        :param hauteur_objet: La hauteur de l'objet à ajouter
        :param nom_objet: La désignation de l'objet
        :return: True si réussi sinon False
        """
        # Parcours du wagon entier où l'objet pourrait être placé sans dépasser ses dimensions
        for i in range(longueur_wagon - longueur_objet + 1):
            for j in range(largeur_wagon - largeur_objet + 1):
                for k in range(hauteur_wagon - hauteur_objet + 1):
                    # Vérification de l'espace libre pour l'objet
                    if all(wagon["espace"][i + x][j + y][k + z] == 0 for x in range(longueur_objet) for y in
                           range(largeur_objet) for z in range(hauteur_objet)):
                        # Mise en place de l'objet dans le wagon
                        for x in range(longueur_objet):
                            for y in range(largeur_objet):
                                for z in range(hauteur_objet):
                                    wagon["espace"][i + x][j + y][k + z] = 1
                        wagon["items"].append(nom_objet)
                        return True
        return False

    # Recherche les dimensions des objets dans le dictionnaire
    for item in dico.keys():
        longueur_objet = round(float(dico[item][0]) / 0.1)
        largeur_objet = round(float(dico[item][1]) / 0.1)
        hauteur_objet = round(float(dico[item][2]) / 0.1)

        # Placer l'objet dans chaque wagon existant
        for wagon in train:
            if placer_objet(wagon, longueur_objet, largeur_objet, hauteur_objet, item):
                break
        else:
            # Création d'un nouveau wagon si l'objet ne peut pas être placé dans les wagons existants
            new_wagon = creer_wagon()
            train.append(new_wagon)
            if not placer_objet(new_wagon, longueur_objet, largeur_objet, hauteur_objet, item):
                break

    print("On a", len(train), "wagons pour mettre tous les objets dans le train.")
    return train


# ================ Algorithmes offlines =====================
# Best Fit decreasing

def offline1(dico):
    """
    Fonction réalisée Margot assistée par Nicolas
    Rangement en ne prenant en compte que la longueur des marchandises et on peut les trier au départ
    :param dico: Un dictionnaire comportant tous les objets à mettre dans le train
    :return: Une liste de liste qui correspond au train et aux wagons remplis
    """
    train = []
    longueur_wagon = 11.583
    longueur = 0
    wagon = []
    objet_enleve = []
    num = 0

    dimension_totale = 0

    dico_tri = sorted(dico.items(), key=lambda objet: objet[1][0], reverse=True)

    nb_op = 7

    while len(dico_tri) != 0:
        num += 1
        wagon.append(dico_tri[0])
        longueur += dico_tri[0][1][0]
        dimension_totale += float(dico_tri[0][1][0])
        dico_tri.pop(0)
        nb_op += 4

        for i in range(len(dico_tri)):
            if (dico_tri[i][1][0] + longueur <= longueur_wagon):
                wagon.append(dico_tri[i])
                longueur += dico_tri[i][1][0]
                dimension_totale += float(dico_tri[i][1][0])
                objet_enleve.append(i)
                nb_op += 4

        rang = 0
        for objet in objet_enleve:
            # print("rang == ", objet, " longeur dico ==", len(dico_tri))
            dico_tri.pop(objet - rang)
            rang += 1
            nb_op += 2

        objet_enleve.clear()

        # print("Le wagon numéro:",num, "est ", wagon, "et sa longueur est :", longueur)
        train.append(wagon)
        wagon.clear()
        longueur = 0
        nb_op += 5

    print("On a", len(train), "wagons pour mettre tous les objets dans le train.")
    print("Dimensions non utilisées :", len(train) * longueur_wagon - dimension_totale, "mètres")

    # Calcul estimation du temps de calcul
    print("Le nombre d'opérations maximale est :", nb_op)  # => 739 opérations
    print("Le temps maximal estimé pour cet algo est ", nb_op * 1e-7)  # => 7.39e-5 s


def offline2(dico):
    """
    Fonction réalisée par Emir et modifiée par Margot pour la partie de tri
    Rangement en ne prenant en compte que la longueur des marchandises et on peut les trier au départ
    :param dico: Un dictionnaire comportant tous les objets à mettre dans le train
    :return: Une liste de liste qui correspond au train et aux wagons remplis
    """

    # Tri du dictionnaire en fonction de la surface de chaque objet dans l'ordre décroissant
    dico_tri = sorted(dico.items(), key=lambda objet: objet[1][0] * objet[1][1], reverse=True)

    # Dimension du wagon en multiple 0.1
    longueur_wagon = round(11.583 / 0.1)
    largeur_wagon = round(2.294 / 0.1)

    def creer_wagon():
        """
        Création d'un wagon vide
        :return: Un wagon vide, un dictionnaire avec l'espace du wagon sous forme de matrice et les informations des
        objets présents
        """
        return {
            "espace": [[0] * largeur_wagon for w in range(longueur_wagon)],
            "items": []
        }

    # Initialisation du train avec le premier wagon
    train = []
    wagon = creer_wagon()
    train.append(wagon)

    def placer_objet(wagon, longueur_objet, largeur_objet, nom_objet):
        """
        Placer un objet dans le wagon
        :param wagon: Le wagon (une matrice) dans lequel on veut mettre l'objet
        :param longueur_objet: La longueur de l'objet à ajouter
        :param largeur_objet: La largeur de l'objet à ajouter
        :param nom_objet: La désignation de l'objet
        :return: True si réussi sinon False
        """
        # Parcours du wagon entier où l'objet pourrait être placé sans dépasser ses dimensions
        for i in range(longueur_wagon - longueur_objet + 1):
            for j in range(largeur_wagon - largeur_objet + 1):
                # Vérification de l'espace libre pour l'objet
                if all(wagon["espace"][i + x][j + y] == 0 for x in range(longueur_objet) for y in range(largeur_objet)):
                    # Mise en place de l'objet dans le wagon
                    for x in range(longueur_objet):
                        for y in range(largeur_objet):
                            wagon["espace"][i + x][j + y] = 1
                    wagon["items"].append(nom_objet)
                    return True
        return False

    # Recherche les dimensions des objets dans le dictionnaire
    for item in dico_tri:
        longueur_objet = round(float(item[1][0]) / 0.1)
        largeur_objet = round(float(item[1][1]) / 0.1)

        # Placer l'objet dans chaque wagon existant
        for wagon in train:
            if placer_objet(wagon, longueur_objet, largeur_objet, item):
                break
        else:
            # Création d'un nouveau wagon si l'objet ne peut pas être placé dans les wagons existants
            new_wagon = creer_wagon()
            train.append(new_wagon)
            if not placer_objet(new_wagon, longueur_objet, largeur_objet, item):
                break

    print("On a", len(train), "wagons pour mettre tous les objets dans le train.")
    return train


def offline3(dico):
    """
    Fonction réalisée par Emir et modifiée par Margot pour la partie de tri
    Rangement en ne prenant en compte toutes les dimensions (longueur, largeur, hauteur) des marchandises et on peut
    les trier au départ
    :param dico: Un dictionnaire comportant tous les objets à mettre dans le train
    :return: Une liste de liste qui correspond au train et aux wagons remplis
    """
    # Dimension du wagon en multiple 0.1
    longueur_wagon = round(11.583 / 0.1)
    largeur_wagon = round(2.294 / 0.1)
    hauteur_wagon = round(2.569 / 0.1)

    dico_tri = sorted(dico.items(), key=lambda objet: objet[1][0] * objet[1][1] * objet[1][2], reverse=True)

    # Création d'un wagon vide
    def creer_wagon():
        """
        Création d'un wagon vide
        :return: Un wagon vide, un dictionnaire avec l'espace du wagon sous forme de matrice et les informations des
        objets présents
        """
        return {
            "espace": [[[0] * hauteur_wagon for w in range(largeur_wagon)] for w in range(longueur_wagon)],
            "items": []
        }

    # Initialisation du train avec le premier wagon
    train = []
    wagon = creer_wagon()
    train.append(wagon)

    def placer_objet(wagon, longueur_objet, largeur_objet, hauteur_objet, nom_objet):
        """
        Placer un objet dans le wagon
        :param wagon: Le wagon (une matrice) dans lequel on veut mettre l'objet
        :param longueur_objet: La longueur de l'objet à ajouter
        :param largeur_objet: La largeur de l'objet à ajouter
        :param hauteur_objet: La hauteur de l'objet à ajouter
        :param nom_objet: La désignation de l'objet
        :return: True si réussi sinon False
        """
        # Parcours du wagon entier où l'objet pourrait être placé sans dépasser ses dimensions
        for i in range(longueur_wagon - longueur_objet + 1):
            for j in range(largeur_wagon - largeur_objet + 1):
                for k in range(hauteur_wagon - hauteur_objet + 1):
                    # Vérification de l'espace libre pour l'objet
                    if all(wagon["espace"][i + x][j + y][k + z] == 0 for x in range(longueur_objet) for y in
                           range(largeur_objet) for z in range(hauteur_objet)):
                        # Mise en place de l'objet dans le wagon
                        for x in range(longueur_objet):
                            for y in range(largeur_objet):
                                for z in range(hauteur_objet):
                                    wagon["espace"][i + x][j + y][k + z] = 1
                        wagon["items"].append(nom_objet)
                        return True
        return False

    # Recherche les dimensions des objets dans le dictionnaire
    for item in dico_tri:
        longueur_objet = round(float(item[1][0]) / 0.1)
        largeur_objet = round(float(item[1][1]) / 0.1)
        hauteur_objet = round(float(item[1][2]) / 0.1)

        # Placer l'objet dans chaque wagon existant
        for wagon in train:
            if placer_objet(wagon, longueur_objet, largeur_objet, hauteur_objet, item):
                break
        else:
            # Création d'un nouveau wagon si l'objet ne peut pas être placé dans les wagons existants
            new_wagon = creer_wagon()
            train.append(new_wagon)
            if not placer_objet(new_wagon, longueur_objet, largeur_objet, hauteur_objet, item):
                break

    print("On a", len(train), "wagons pour mettre tous les objets dans le train.")
    return train
