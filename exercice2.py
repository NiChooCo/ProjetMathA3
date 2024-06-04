import pandas as pd

def create_dico(datapath):
    """
    Créer un dictionnaire avec les données du csv
    :param datapath: chemin vers le fichier csv
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
    :param dico:
    :return:
    """
    train = []
    longueur_wagon = 11.583
    longueur = 0
    wagon = []

    for item in dico.keys():
        if(longueur+float(dico[item][0]) < longueur_wagon):
            wagon.append(item)
            longueur += float(dico[item][0])
        else:
            train.append(wagon)
            wagon.clear()
            longueur = 0
            wagon.append(item)
            longueur += float(dico[item][0])

    print("On a", len(train), "wagons pour mettre tous les objets dans le train.")

def online2(dico):
    """
    Rangement en ne prenant en compte que la longeur et la largeur des marchandises et on ne peut pas les trier au départ.
    :param dico:
    :return:
    """
    pass

def online3(dico):
    """
    Rangement en ne prenant en compte toutes les dimmensions (longeur, largeur, hauteur) des marchandises et on ne peut
    pas les trier au départ.
    :param dico:
    :return:
    """
    pass

def offline1(dico):
    """
    Rangement en ne prenant en compte que la longeur des marchandises et on peut les trier au départ
    :param dico:
    :return:
    """
    train = []
    longueur_wagon = 11.583
    longueur = 0
    wagon = []
    dico_tri = sorted(dico.items(), key=lambda objet: objet[1][0], reverse=True)
    while len(dico_tri) != 0:
        wagon.append(dico_tri[0])
        longueur_wagon -= dico_tri[0][1][0]
        dico_tri.pop(0)

        # TO DO : OUT OF RANGE
        for i in range(len(dico_tri)):
            if(dico_tri[i][1][0] + longueur_wagon <= 11.583):
                wagon.append(dico_tri[i])
                longueur_wagon -= dico_tri[i][1][0]
                dico_tri.pop(i)


        train.append(wagon)
        wagon.clear()
        longueur_wagon = 11.583

    print("On a", len(train), "wagons pour mettre tous les objets dans le train.")

def offline2(dico):
    """
    Rangement en ne prenant en compte que la longeur des marchandises et on peut les trier au départ
    :param dico:
    :return:
    """
    pass

def offline3(dico):
    """
    Rangement en ne prenant en compte toutes les dimmensions (longeur, largeur, hauteur) des marchandises et on peut les
    trier au départ
    :return:
    """
    pass