import numpy as np


def question1_2():
    n_objets = [1, 2, 10, 23]
    print("Question 1 :")
    for i in n_objets:
        print("Nombre de possibilités pour", i, "objets:", 2**i)
    print("\nQuestion2 :\nNombre max de possibilités :", 2**max(n_objets))


if __name__ == '__main__':
    question1_2()
