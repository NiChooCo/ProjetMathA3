import pandas as pd

data = pd.read_csv("Donnees_marchandises.csv", header=0, delimiter=";")

def create_dico(data):
    """
    Créer un dictionnaire avec les données du csv
    :param data: csv
    :return: a dict
    Numéro
    Désignation
    Longueur
    Largeur
    Hauteur
    """
    new = {}
    for i in range(len(data)):
        if(data["Désignation"][i] in new.keys()):
            new_name = data["Désignation"][i] + str(i)
            new[new_name] = [data["Longueur"][i], data["Largeur"][i], data["Hauteur"][i]]
        else:
            new[data["Désignation"][i]] = [data["Longueur"][i], data["Largeur"][i], data["Hauteur"][i]]

    #print(new)
    return(new)


def online1():
    """
    Rangement en ne prenant en compte que la longeur des marchandises et on ne peut pas les trier au départ.
    :return:
    """
    print(data)

def online2():
    """
    Rangement en ne prenant en compte que la longeur et la largeur des marchandises et on ne peut pas les trier au départ.
    :return:
    """
    pass

def online3():
    """
    Rangement en ne prenant en compte toutes les dimmensions (longeur, largeur, hauteur) des marchandises et on ne peut
    pas les trier au départ.
    :return:
    """
    pass

def offline1():
    """
    Rangement en ne prenant en compte que la longeur des marchandises et on peut les trier au départ
    :return:
    """
    pass

def offline2():
    """
    Rangement en ne prenant en compte que la longeur des marchandises et on peut les trier au départ
    :return:
    """
    pass

def offline3():
    """
    Rangement en ne prenant en compte toutes les dimmensions (longeur, largeur, hauteur) des marchandises et on peut les
    trier au départ
    :return:
    """
    pass