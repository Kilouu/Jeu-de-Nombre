# Created by Naashy
# Date : 15/03/2020
# Le Programme est un jeu de Nombre


from random import *
import os 

# Un nombre aléatoire est choisit par le programme

n = randint(1,1000)

# Mettre print(n) si vous souhaitez tester le programme en vous affichant la réponse dès le débuts

print(n)

# Présentation

print("Le but de ce jeux est de trouver le nombre exacte auquel le Robots pense.")
print("J'espère que ce jeu va te plaire")
print("Bonne Chance")

# Début du programme

number = int(input("Entrer un numéro entre 1 et 1000 : "))

# Le joueur à le droit à 20 essaies

for i in range(1,20):

    if number==n :
        print("Bien joué")
        print("Nombre d'essai : ", i)
        stop = print(input("Le programme est finit, appuyer sur la Touche 'entrée' pour arréter"))
        quit()

    elif number>n :
        print("C'est moins - ")

    else:
        print("C'est plus + ")
    
    number = int(input("Entrer un numéro entre 1 et 1000 : "))

print("Perdu en 20 coup")

stop = print(input("Le programme est finit, appuye sur la Touche 'entrée' pour arréter"))
quit()

# Fin ©
# Discord : Naashy#8434
# My GitHub : https://github.com/Naashy
