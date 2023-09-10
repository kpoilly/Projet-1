"""
POILLY Kilyan
000460014
B1-INFO
Groupe 6
"""

from turtle import *
import os
from random import randint

def draw_wordline(lenm):
    """
    Fonction qui dessine les traits correspondant aux lettres.
    """
    pendown()
    forward(30)
    penup()
    forward(7)

def draw_letter(jeu):
    """
    Fonction qui écrit la lettre du mot trouvée par le joueur.
    """
    write(jeu, False, "center", font=("Arial", 20, "normal"))

def draw_error(jeu, lettererror):
    """
    Fonction qui écrit les lettres données par le joueur qui ne
    sont pas dans le mot.
    """
    penup()
    goto(-350+20*lettererror, -350)
    write(jeu, False, "center", font=("Arial", 15, "normal"))
    
def draw_pendu(error):
    """
    Fonction qui dessine le dessin du pendu, qui poursuit un peu
    plus le dessin à chaque fois que le joueur donne une lettre
    qui n'est pas dans le mot.
    """
    if error == 1: #Potence
        penup()
        goto(0,-50)
        backward(200)
        pendown()
        forward(400)
        penup()
        backward(300)
        pendown()
        left(90)
        forward(300)
        right(90)
        forward(150)
        right(90)
        forward(50)
        left(90)
    elif error == 2: #Tête
        penup()
        goto(50, 200)
        pendown()
        left(180)
        circle(25)
        left(90)
        penup()
        forward(50)
        left(90)
    elif error == 3: #Corps
        penup()
        goto(50, 150)
        right(90)
        pendown()
        forward(100)
        left(90)
    elif error == 4: #Bras droit
        penup()
        goto(50, 50)
        right(90)
        penup()
        backward(75)
        left(45)
        pendown()
        forward(45)
        penup()
        backward(45)
        left(45)
    elif error == 5: #Bras gauche
        penup()
        goto(50, 125)
        right(135)
        pendown()
        forward(45)
        penup()
        backward(45)
        left(135)
    elif error == 6: #Jambe droite
        penup()
        goto(50, 125)
        right(90)
        forward(75)
        left(45)
        pendown()
        forward(45)
        penup()
        backward(45)
        left(45)
    elif error == 7: #Jambe Gauche
        penup()
        goto(50, 50)
        right(135)
        pendown()
        forward(45)
        penup()
        backward(45)
        left(45)

def end(error, points, motjeu):
    """
    Fonction qui gère la fin du jeu, vérifie si le joueur a
    perdu ou gagné et affiche le résultat.
    """

    if error == 7:
        win = False
        bgcolor("red")
        penup()
        goto(-50, -100)
        write("Perdu !", font=("Arial", 25, "normal"))
        goto(41, 180)
        setheading(0)
        pendown()
        dot()
        penup()
        forward(16)
        pendown()
        dot()
        penup()
        goto(60, 160)
        setheading(90)
        pendown()
        circle(10, 180)
    
    elif points == len(motjeu):
        bgcolor("green")
        penup()
        goto(-50, -100)
        write("Gagné !", font=("Arial", 25, "normal"))
        goto(41, 180)
        setheading(0)
        pendown()
        if error >= 2 :
            dot()
            penup()
            forward(16)
            pendown()
            dot()
            penup()
            goto(40, 170)
            setheading(-90)
            pendown()
            circle(10, 180)
        
def reset():
    """
    Fonction qui demande au joueur s'il souhaite rejouer, si oui,
    relance la fonction jeu(), sinon ferme la fenêtre turtle et le
    programme.
    """
    resetv = textinput("Rejouer ?", "Tapez OUI ou NON")
    resetv = resetv.lower()

    if resetv == "oui":
        clear()
        jeu()
    elif resetv == "non":
        bye()
    else :
        reset()
    

def jeu():
    """
    Fonction qui gère la plus grosse partie du jeu et les appels
    aux autres fonctions, mise sous forme de fonction pour
    faciliter le restart du jeu.
    """
    title("Le Jeu du Pendu !")
    hideturtle()
    setheading(0)
    bgcolor("white")
    docmot = open('mots.txt', 'r')
    motsl = []
    for i in docmot:
        motsl.append(i.strip())
    docmot.close()
    a = randint(0,len(motsl))
    motjeu = list(motsl[a-1])
    lenm = len(motjeu)/2
    trouves = [] #Liste des lettres trouvées, pour ne pas compter 2
                 #points pour la même lettre.
    fausses = [] #Liste des lettres fausses, pour ne pas afficher 2
                 #fois la même lettre.
    lettererror = 0
    error = 0    #2 variables error, une qui va augmenter à chaque fois
                 #que le joueur fait une erreur (error) pour poursuivre
                 #le dessin, l'autre (lettererror) qui ne va augmenter
                 #que si le joueur entre une fausse lettre qu'il n'a pas
                 #déjà entré.
    x = 0
    points = 0
    penup()
    goto(0, -250)
    backward(lenm*37)
    hideturtle()

    while x < len(motjeu) :
        draw_wordline(lenm)
        x = x+1

    goto(-390, -350)
    write("Fausses :", False, "center", font=("Arial", 15, "underline"))

    while error < 7 and points < len(motjeu) :
        jeu = textinput("Lettre : ","Entrez une lettre :")
        jeu = jeu.lower()
        if jeu not in trouves:
            if jeu in motjeu :
                for i in range(len(motjeu)):
                    penup()
                    goto((-37*lenm)+15, -247)
                    if jeu == motjeu[i] :
                        forward(37*i)
                        draw_letter(jeu)
                        points = points +1
                        trouves.append(jeu)
            elif len(jeu) != 1:
                pass
            else:
                error = error +1
                if jeu not in fausses :
                    lettererror = lettererror +1
                    draw_error(jeu, lettererror)
                    fausses.append(jeu)
                draw_pendu(error)

    end(error, points, motjeu)
    reset()

jeu()
print("Merci d'avoir joué !")
