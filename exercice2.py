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
    Rangement en ne prenant en compte que la longueur des marchandises et on ne peut pas les trier au départ.
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
    Rangement en ne prenant en compte que la longueur et la largeur des marchandises et on ne peut pas les trier au départ.
    :param dico:
    :return:
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
            train.append([item])
        else:
            for i in range(len(train)):

                if tab_longueur[i] > float(dico2[item][0]) and tab_longueur[i]-float(dico2[item][0])>0:
                    tab_longueur[i] -= float(dico2[item][0])
                    train[i].append(dico[item])
                    #dico2.pop(item)
                    break

                elif tab_largeur[i] > float(dico2[item][1]) and tab_largeur[i] - float(dico[item][1])>0:
                    tab_largeur[i] -= float(dico2[item][1])
                    train[i].append(dico[item])
                    tab_longueur[i] = longueur_wagon - float(dico2[item][0])
                    #dico2.pop(item)
                    break

                #print("Train à l'étape", i , "==<>",train[i])
            else:
                tab_longueur.append(longueur_wagon - float(dico2[item][0]))
                tab_largeur.append(largeur_wagon - float(dico2[item][1]))
                train.append(dico[item])

    print(train)
    print("On a", len(train), "wagons pour mettre tous les objets dans le train.")

def online3(dico):
    """
    Rangement en ne prenant en compte toutes les dimensions (longueur, largeur, hauteur) des marchandises et on ne peut
    pas les trier au départ.
    :param dico:
    :return:
    """
    pass

def offline1(dico):
    """
    Rangement en ne prenant en compte que la longueur des marchandises et on peut les trier au départ
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

    nb_op = 7

    while len(dico_tri) != 0:
        num += 1
        wagon.append(dico_tri[0])
        longueur += dico_tri[0][1][0]
        dico_tri.pop(0)
        nb_op += 4

        for i in range(len(dico_tri)):
            if(dico_tri[i][1][0] + longueur <= longueur_wagon):
                wagon.append(dico_tri[i])
                longueur += dico_tri[i][1][0]
                objet_enleve.append(i)
                nb_op += 4

        rang = 0
        for objet in objet_enleve:
            #print("rang == ", objet, " longeur dico ==", len(dico_tri))
            dico_tri.pop(objet-rang)
            rang += 1
            nb_op += 2

        objet_enleve.clear()

        #print("Le wagon numéro:",num, "est ", wagon, "et sa longueur est :", longueur)
        train.append(wagon)
        wagon.clear()
        longueur = 0
        nb_op += 5

    print("On a", len(train), "wagons pour mettre tous les objets dans le train.")

    # Calcul estimation du temps de calcul
    print("Le nombre d'opérations maximale est :", nb_op) # => 739 opérations
    print("Le temps maximal estimé pour cet algo est ", nb_op*1e-6) # => 7.39e-4 s

def offline2(dico):
    """
    Rangement en ne prenant en compte que la longueur des marchandises et on peut les trier au départ
    :param dico:
    :return:
    """
    longueur_wagon = 11.583
    largeur_wagon = 2.294

    train = []
    longueur = 0
    wagon = []
    objet_enleve = []
    num = 0

    dico_tri = sorted(dico.items(), key=lambda objet: objet[1][0]*objet[1][1], reverse=True)


def offline3(dico):
    """
    Rangement en ne prenant en compte toutes les dimensions (longueur, largeur, hauteur) des marchandises et on peut les
    trier au départ
    :return:
    """
    longueur_wagon = 11.583
    largeur_wagon = 2.294
    hauteur_wagon = 2.569

    train = []
    longueur = 0
    wagon = []
    objet_enleve = []
    num = 0

    dico_tri = sorted(dico.items(), key=lambda objet: objet[1][0] * objet[1][1]*objet[1][2], reverse=True)