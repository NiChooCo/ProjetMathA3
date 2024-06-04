import panda as pd


def A():
    data = pd.read_csv("TabDonneesSac.csv", sep=';', header=0)
    masse = data['Masse']
    utilite = data['Utilite']