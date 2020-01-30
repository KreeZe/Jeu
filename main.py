#Jeu Fait Par Yamis MANFALOTI

"""
Librairies
"""

import pygame
from random import*

"""
Initialisation pygame + paramètre
"""
pygame.init()
infoObject = pygame.display.Info()
fenetre = pygame.display.set_mode((infoObject.current_w-100, infoObject.current_h-100))
pygame.display.set_caption("Jeu")
font = pygame.font.Font('freesansbold.ttf', 20)

"""
Fonction Main
"""

def main():
    print("ab")


"""
Menu Du Jeux
"""

def menu():
    print("-----------------------------------------------------")
    print("1 - Jouer Au Jeu")
    print("2 - Quitter")
    print("-----------------------------------------------------")
    choix = str(input("choix"))
    if choix == '1':
        main()
    elif choix == '2':
        print("Au Revoir")
        pygame.quit()


"""
Execution
"""

menu()