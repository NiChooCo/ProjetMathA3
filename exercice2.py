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
    tab_longueur = []
    for item in dico.keys():
        if not train:
            tab_longueur.append(longueur_wagon - float(dico[item][0]))
            train.append([item])
        else:
            for i in range(len(train)):
                if tab_longueur[i] >= float(dico[item][0]):
                    tab_longueur[i] -= float(dico[item][0])
                    train[i].append(item)
                    break
            else:
                tab_longueur.append(longueur_wagon - float(dico[item][0]))
                train.append([item])

    print(train)
    print(tab_longueur)
    print("On a", len(train), "wagons pour mettre tous les objets dans le train.")


    '''for item in list(dico.keys()):
        for l in range(len(tab_longueur)-1):
            if tab_longueur[l] >= float(dico[item][0]) and tab_longueur[l] - float(dico[item][0]) >= 0:
                tab_longueur[l] -= float(dico[item][0])
                train[l].append(item)
                print(train)
        else:
            wagon.append(item)
            train.append(wagon)
            print("Le wagon est ==>", wagon)
            # wagon.clear()
            tab_longueur.append(longueur_wagon - float(dico[item][0]))
            print(tab_longueur)
            longueur = 0
            longueur += float(dico[item][0])

    print(train)
    print("On a", len(train), "wagons pour mettre tous les objets dans le train.")'''

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
    objet_enleve = []
    num=0

    dico_tri = sorted(dico.items(), key=lambda objet: objet[1][0], reverse=True)

    while len(dico_tri) != 0:
        num+=1
        wagon.append(dico_tri[0])
        longueur += dico_tri[0][1][0]
        dico_tri.pop(0)

        # TO DO : Objet qui s'enlève pas bien
        for i in range(len(dico_tri)-1):
            if(dico_tri[i][1][0] + longueur <= longueur_wagon):
                wagon.append(dico_tri[i])
                longueur += dico_tri[i][1][0]
                objet_enleve.append(i)

        rang = 0
        for objet in objet_enleve:
            print("rang == ", objet, " longeur dico ==", len(dico_tri))
            dico_tri.pop(objet-rang)
            rang += 1
        objet_enleve.clear()

        print("Le wagon numéro:",num, "est ", wagon)
        train.append(wagon)
        wagon.clear()
        longueur = 0

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