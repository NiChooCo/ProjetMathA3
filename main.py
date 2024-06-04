import numpy as np
import csv
from time import time
import Margot_test as m
import Test_Nico as n
from exercice1 import *


# Question 3 :
# Utilité maximale pour un poids inférieur ou égal à 0.6 : 7.6 avec 6 objets pour un poids total de 0.6


if __name__ == '__main__':
    #question1_2()

    #m.question5(4000)
    """Estimations temps:
        Affectation, addition, soustraction => 2,5e-8
        Multiplication, Division => 1e-7
        
        Comme on doit choisir le même temps pour chaque on a choisi 1e-7
    """

    # Il faut tester
    #tps = (2**23) * (2.5e-8) * 2
    #print('Le temps estimé pour tester toutes les combinaisons est :', tps, ' secondes.')


    # Question 14
    #start = time()
    #m.algo_B(5)
    #stop = time()

    #print("Le temps de l'ago B est : ", stop- start, " seconde.")
    # Pour C = 2; vrai temps = 1.08e-4 secondes ; temps estimé = 2.149e-5
    # Pour C = 3; vrai temps = 1.07e-4 secondes ; temps estimé = 2.149e-5
    # Pour C = 4; vrai temps = 1.13e-4 secondes ; temps estimé = 2.149e-5
    # Pour C = 5; vrai temps = 1.20e-4 secondes ; temps estimé = 2.149e-5

    #m.algo_A(3)
    #print(dico)
    n.question10(2)
    # Temps d'exécution : 263.7648513317108
    n.question10(3)
    # Temps d'exécution : 263.69722151756287
    n.question10(4)
    # Temps d'exécution : 263.74284648895264
    n.question10(5)
    # Temps d'exécution : 262.98826360702515
