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



def question5(n):
    start = time()
    # Il faut varier l'opération et le n pour tester les différentes opérations
    for i in range(n):
        op = 36 / 39
    stop = time()

    print(stop-start)

def algo_A(n):
    #Méthode pas concluante
    #data = pd.read_csv("TabDonneesSac.csv", sep=';', header=0).to_dict()
    #poids = data["Masse"]
    #utilite = data["Utilité"]
    #ratio = []

    for key in dico.keys():
        dico[key].append(dico[key][1]/dico[key][0])

    dico_tri = sorted(dico.items(), key=lambda truc:truc[1][2], reverse=True)



    print(dico_tri)


