import numpy as np
import csv
from time import time
import Margot_test as m

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


def question1_2():
    n_objets = [1, 2, 10, 23]
    print("Question 1 :")
    for i in n_objets:
        print("Nombre de possibilités pour", i, "objets:", 2**i)
    print("\nQuestion2 :\nNombre max de possibilités :", 2**max(n_objets))


# Question 3 :
# Utilité maximale pour un poids inférieur ou égal à 0.6 : 7.6 avec 6 objets pour un poids total de 0.6


if __name__ == '__main__':
    #question1_2()

    m.question5(4000)
    """Estimations temps:
        Affectation, addition, soustraction => 2,5e-8
        Multiplication, Division => 1e-7
    """
    # Il faut tester
    #tps = (2**23) * (2.5e-8) * 2
    #print('Le temps estimé pour tester toutes les combinaisons est :', tps, ' secondes.')

    start = time()
    m.algo_B(5)
    stop = time()

    print("Le temps de l'ago B est : ", stop- start, " seconde.")
    # Pour C = 2; temps = 3.09e-5 secondes
    # Pour C = 3; temps = 2.88e-5 secondes
    # Pour C = 4; temps = 2.38e-5 secondes
    # Pour C = 5; temps = 3.52e-5 secondes
