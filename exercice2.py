import pandas as pd

def create_dico(datapath):
    """
    Créer un dictionnaire avec les données du csv
    :param data: chemin vers le fichier csv
    :return: a dict
    """
    data = pd.read_csv(datapath, header=0, delimiter=";")
    new = {}
    for i in range(len(data)):
        if(data["Désignation"][i] in new.keys()):
            new_name = data["Désignation"][i] + str(i)
            new[new_name] = [data["Longueur"][i], data["Largeur"][i], data["Hauteur"][i]]
        else:
            new[data["Désignation"][i]] = [data["Longueur"][i], data["Largeur"][i], data["Hauteur"][i]]

    #print(new)
    return(new)

# Pour cette partie utiliser First Fit decreasing et Best Fit decreasing

def online1(dico):
    """
    Rangement en ne prenant en compte que la longeur des marchandises et on ne peut pas les trier au départ.
    :return:
    """


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