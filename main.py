from time import time
from exercice1 import *
from exercice2 import *

if __name__ == '__main__':
    # ================== Partie 1 =======================

    # ----------- Question 1 et 2 -----------
    # n_objets = [1, 2, 10, 23]
    # question1_2()

    # ------------ Question 3 ---------------
    ''' Utilité maximale pour un poids inférieur ou égal à 0.6 : 7.6 avec 6 objets pour un poids total de 0.6 '''

    # ---------- Tests pour la question 5 ------------
    # question5(4000)
    '''
    Estimations temps:
        Affectation, addition, soustraction => 2,5e-8
        Multiplication, Division => 1e-7
        
    Comme on doit choisir le même temps pour chaque on a choisi 1e-7
    '''

    # ------------ Réponse pour la question 6 ------------------

    # Il faut tester
    # tps = (2**23) * (2.5e-7) * 2
    # print('Le temps estimé pour tester toutes les combinaisons est :', tps, ' secondes.')

    # ------- Tests pour la question 8 ----------
    # -- Première méthode exacte --
    # bruteforce(0.6, dico_objet)

    # bruteforce(2, dico_objet)
    ''' Temps d'exécution : 263.7648513317108 '''

    # bruteforce(3, dico_objet)
    ''' Temps d'exécution : 263.69722151756287 '''

    # bruteforce(4, dico_objet)
    ''' Temps d'exécution : 263.74284648895264 '''

    # bruteforce(5, dico_objet)
    ''' Temps d'exécution : 262.98826360702515 '''

    # -- Troisième méthode exacte --
    # tree(dico_exact, 2)

    # Affichage des sous-ensembles
    # start_time = time()
    # for subset, weight in tree(dico_exact):
    #    if weight == 0.6:
    #        print("Objets:", subset, " Poids:", weight)

    # end_time = time()
    # print(f"Temps d'exécution : {end_time - start_time:.4f} secondes")

    # ----- Question 11 -----

    # recherche_locale(2, dico_objet)

    # recherche_locale(3, dico_objet)

    # recherche_locale(4, dico_objet)

    # recherche_locale(5, dico_objet)

    # ----- Question 14 -----

    # start = time()
    # algo_B(5, dico_objet)
    # stop = time()

    # print("Le temps de l'ago B est : ", stop- start, " seconde.")
    ''' 
    Pour C = 2; vrai temps = 1.08e-4 secondes ; temps estimé = 2.149e-5
    Pour C = 3; vrai temps = 1.07e-4 secondes ; temps estimé = 2.149e-5
    Pour C = 4; vrai temps = 1.13e-4 secondes ; temps estimé = 2.149e-5
    Pour C = 5; vrai temps = 1.20e-4 secondes ; temps estimé = 2.149e-5
    '''

    # ================== Partie 2 =======================

    dico = create_dico("Donnees_marchandises.csv")

    start = time()
    # Tests pour 1 dimension

    # offline1(dico)
    # online1(dico)

    # Test pour 2 dimensions

    # train2 = online2(dico) # Ne fonctionne pas correctement
    # train2 = online2_emir(dico)
    # train2 = offline2(dico)

    volume_total = 0
    # for i, wagon in enumerate(train2):
    #     volume = volume_libre_2d(wagon)
    #    volume_total += volume
    #    print(f"Wagon {i + 1} contient les objets : {wagon['items']}")
    #    print(f"Wagon {i + 1} : {wagon['espace']}")
    #    print(f"Wagon {i + 1} a un volume libre de : {volume:.3f} m^2\n")
    # print(f"Volume total libre : {volume_total:.3f} m^2")

    # Tests pour 3 dimensions

    # train3 = online3(dico)
    train3 = offline3(dico)

    # volume_total = 0
    # for i, wagon in enumerate(train3):
    #     volume = volume_libre_3d(wagon)
    #     volume_total += volume
    #     print(f"Wagon {i + 1} contient les objets : {wagon['items']}")
    #     print(f"Wagon {i + 1} a un volume libre de : {volume:.3f} m^3")
    # print(f"Volume total libre : {volume_total:.3f} m^3")

    end = time()
    print(f"Temps d'exécution : {end - start:.15f} secondes")
