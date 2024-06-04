import pandas as pd
from time import time


def question5(n):
    start = time()
    # Il faut varier l'opération et le n pour tester les différentes opérations
    for i in range(n):
        op = 36 / 39
    stop = time()

    print(stop-start)

def algo_A(n):
    data = pd.read_csv("TabDonneesSac.csv", sep=';', header=0).to_dict()

    print(data)

    '''
    dico{(poids[i],utilité[i]) : ratio[i]}
    '''

    poids = data["Masse"]
    utilite = data["Utilité"]

    print(poids)
    ratio = []
    for i in range(len(poids)):
        ratio.append(float(utilite[i])/float(poids[i]))

    data["ratio"] = ratio
    print(data["ratio"])
