"""
Programme réalisé par nom, prénom, classe
"""
from random import*
import pygame

#variables du niveau
NB_TILES = 17   #nombre de tiles a chager (ici de 00.png à 26.png) 27 au total !!
TITLE_SIZE=48   #definition du dessin (carré)
largeur=15    #hauteur du niveau
hauteur=15    #largeur du niveau
tiles=[]        #liste d'images tiles

#variables de gestion du pacman
joueurX=1          #position x y du pacman dans le niveau
joueurY=2
compteurBilles=0

#variables de gestion du ennemie
FRAMERATE_ennemie= 10    #vitesse du ennemie chiffre elevé = vitesse lente
NB_DEPLACEMENT_ennemie = 17  #le ennemie se deplace sur 9 cases
positionennemie=1
frameRateCounterennemie=0
posfX=1     #position initiale du ennemie
posfY=8

#definition du niveau

plan =[
[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15],
[15,0,0,0,0,0,0,0,0,0,0,0,0,0,15],
[15,0,0,0,0,0,0,0,0,0,0,0,0,0,15],
[15,0,0,0,0,0,0,0,0,0,0,0,0,0,15],
[15,0,0,0,0,0,0,0,0,0,0,0,0,0,15],
[15,0,0,0,0,0,0,0,0,0,0,0,0,0,15],
[15,0,0,0,0,0,0,0,0,0,0,0,0,0,15],
[15,0,0,0,0,0,0,0,0,0,0,0,0,0,15],
[15,0,0,0,0,0,0,0,0,0,0,0,0,0,15],
[15,0,0,0,0,0,0,0,0,0,0,0,0,0,15],
[15,0,0,0,0,0,0,0,0,0,0,0,0,0,15],
[15,0,0,0,0,0,0,0,0,0,0,0,0,0,15],
[15,0,0,0,0,0,0,0,0,0,0,0,0,0,15],
[15,0,0,0,0,0,0,0,0,0,0,0,0,0,15],
[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15]]

"""
[1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2],
[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[3,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4]]
"""

ennemieVierge  = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] ]



#la taille de la fenetre dépend de la largeur et de la hauteur du niveau
#on rajoute une rangée de 32 pixels en bas de la fentre pour afficher le score d'ou (hauteur +1)
pygame.init()
fenetre = pygame.display.set_mode((largeur*TITLE_SIZE, (hauteur+1)*TITLE_SIZE))
pygame.display.set_caption("Pac-Man")
font = pygame.font.Font('freesansbold.ttf', 20)

def emplacementCoffre(plan):
    niveau = plan
    positonCoffreY = randint(6,11)
    positonCoffreX = randint(6,11)
    niveau[positonCoffreY][positonCoffreX] = 14
    return niveau

def parcourEnnemie(positionCoffreXY):
    compte = 1
    ennemie = ennemieVierge
    posCoffreY = positionCoffreXY [0]
    posCoffreX = positionCoffreXY [1]
    departEnnemieY = posCoffreY-2
    departEnnemieX = posCoffreX-2

    for l1 in range(departEnnemieX,departEnnemieX+4):
        ennemie[departEnnemieY][l1] = compte
        compte += 1

    for c1 in range(departEnnemieY,departEnnemieY+4):
        ennemie[c1][departEnnemieX+4] = compte
        compte += 1

    for l2 in range(departEnnemieX+4,departEnnemieX,-1):
        ennemie[departEnnemieY+4][l2] = compte
        compte += 1

    for c2 in range(departEnnemieY+4,departEnnemieY,-1):
        ennemie[c2][departEnnemieX] = compte
        compte += 1

    return ennemie

def chargetiles(tiles):

    #fonction permettant de charger les images tiles dans une liste tiles[]

    for n in range(0,NB_TILES):
        #print('data/'+str(n)+'.png')
        tiles.append(pygame.image.load('data/'+str(n)+'.png')) #attention au chemin


def afficheNiveau(niveau):

    #affiche le niveau a partir de la liste a deux dimensions niveau[][]

    for y in range(hauteur):
        for x in range(largeur):
            fenetre.blit(tiles[niveau[y][x]],(x*TITLE_SIZE,y*TITLE_SIZE))


def affichePac(numero):

    #affiche le pacman en position joueurX et joueurY

    bas = tiles[numero].convert_alpha()
    haut = tiles[16].convert_alpha()
    fenetre.blit(tiles[numero],(joueurX * TITLE_SIZE,joueurY * TITLE_SIZE))
    fenetre.blit(tiles[16],(joueurX * TITLE_SIZE,joueurY * TITLE_SIZE-48))


def rechercheennemie(ennemie,position): #recherche les coord du ennemie dans la liste ennemie

    #recherche les coordonnées du ennemie en fonction du numéro de sa postion dans le parcours

    print(position)                     #la position doit etre dans la liste ennemie sinon plantage
    for y in range(hauteur):
        for x in range(largeur):
            if ennemie[y][x]==position:
                coodennemie=x,y
                global coodennemie
    return coodennemie       #les coord du ennemie x et y sont dans un tuple coodennemie

def deplaceennemie(ennemie):

    #Incrémente automatiquement le déplacement du ennemie, gère sa vitesse et son affichage

    global frameRateCounterennemie
    global positionennemie
    global posfX,posfY
    if frameRateCounterennemie==FRAMERATE_ennemie:      #ralenti la viteese du ennemie
        posfX,posfY=rechercheennemie(ennemie,positionennemie)   #deballage du tuple coordonnées du ennemie
        positionennemie+=1
        if positionennemie==NB_DEPLACEMENT_ennemie:     #un tour est fait donc on passe à la 1ere position
            positionennemie=1
        frameRateCounterennemie=0                       #compteur de vitesse à zero
    fantome = tiles[13].convert_alpha()
    fenetre.blit(fantome,(posfX * TITLE_SIZE,posfY * TITLE_SIZE)) #affichage du ennemie
    frameRateCounterennemie+=1                          #incrémentation du compteur de vitesse


chargetiles(tiles)  #chargement des images
rebours = 0
vie = 3
temps = pygame.time.get_ticks()
fois = 0
coffre = 0

niveau = emplacementCoffre(plan)
loop=True
while loop==True:
    ennemie = ennemieVierge
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_UP:    #est-ce la touche UP
                posY = joueurY - 1             #on deplace le pacman vituellement
                posX = joueurX
                numeroTile = niveau[posY][posX]       #on regarde le numéro du tile
                print("up",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile == 14):      #si le tile est une bille ou un fond noir alors le déplacement est possible
                    joueurY -= 1                               #on monte donc il faut décrémenter pacY
                    print("deplacement possible",joueurX,joueurY)
                else:
                    print("deplacement impossible")
            elif event.key == pygame.K_DOWN:
                posY = joueurY + 1
                posX = joueurX
                numeroTile = niveau[posY][posX]
                print("up",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile == 14):
                    joueurY += 1
                    print("deplacement possible",joueurX,joueurY)
                else:
                    print("deplacement impossible")
            elif event.key == pygame.K_RIGHT:
                posY = joueurY
                posX = joueurX + 1
                numeroTile = niveau[posY][posX]
                print("up",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile == 14):
                    joueurX += 1
                    print("deplacement possible",joueurX,joueurY)
                else:
                    print("deplacement impossible")
            elif event.key == pygame.K_LEFT:
                posY = joueurY
                posX = joueurX - 1
                numeroTile = niveau[posY][posX]
                print("up",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile == 14):
                    joueurX -= 1
                    print("deplacement possible",joueurX,joueurY)
                else:
                    print("deplacement impossible")
            elif event.key == pygame.K_ESCAPE:
                loop = False

    fenetre.fill((0,0,0))   #efface la fenetre
    afficheNiveau(niveau)   #affiche le niveau
    affichePac(12)

    def positionCoffre(niveau):
        for y in range(0,hauteur):
            for x in range (0,largeur):
                if niveau[y][x] == 14:
                    posCoffre = y,x
                    return posCoffre

    positionCoffreXY = positionCoffre(niveau)
    posCoffreY = positionCoffreXY [0]
    posCoffreX = positionCoffreXY [1]

    def spawnEnnemie():
        ennemie = parcourEnnemie(positionCoffreXY)
        deplaceennemie(ennemie) #mettre un commentaire pour desactiver le déplacement du ennemie
    spawnEnnemie()


    numeroTile = niveau[joueurY][joueurX]
    if numeroTile == 14:
        print("vous avez trouver un coffre")
        coffre = 1
        joueurX = 1
        joueurY = 2
    elif niveau[joueurY-1][joueurX] == 14:
        print("vous avez trouver un coffre")
        coffre = 1
        joueurX = 1
        joueurY = 2
    if (posfY,posfX) == (joueurY,joueurX):
        vie = vie - 1
        print("vie -1")

    if coffre == 1:
        niveau[posCoffreY][posCoffreX] = 0
        niveau = emplacementCoffre(plan)
        posfY = posCoffreY - 2
        posfX = posCoffreX - 2
        spawnEnnemie()
        coffre = 0

    if vie == 0:
        loop = False

    pygame.display.update() #mets à jour la fentre graphique


GameOver = True
while GameOver == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GameOver = False

    fenetre.fill((0,0,0))
    font=pygame.font.Font(None, 80)
    text = font.render("Game Over",1,(255,255,255))
    fenetre.blit(text, (largeur*32/3, hauteur*30/2))
    pygame.display.flip()

pygame.quit()

