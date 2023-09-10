from turtle import *
from time import sleep, time
from random import randint
from copy import deepcopy

def Board():
    """
    Initialisation de la grille du jeu et des
    éléments de l'interface utilisateur
    """
    
    board.resizemode("user")
    board.pensize(3)
    board.penup()
    board.goto(-375,-405)
    board.setheading(0)
    board.pendown()
    board.color("white")
    board.begin_fill()
    board.forward(600)
    board.left(90)
    board.forward(810)
    board.left(90)
    board.forward(600)
    board.left(90)
    board.forward(810)
    board.color("#d7dae0")
    board.end_fill()

    board.goto(-375,-385)
    board.setheading(0)
    board.pendown()
    board.begin_fill()
    board.color("white")
    board.forward(600)
    board.left(90)
    board.forward(790)
    board.right(90)
    board.forward(150)
    board.right(90)
    board.forward(810)
    board.right(90)
    board.forward(750)
    board.color('#121c33')
    board.end_fill()
    board.penup()
    board.goto(240,355)
    board.color("white")
    board.write("SCORE : ",False,"left",("Arial", 12, "bold"))
    
    global score
    global Loose

    
    score = 0
    Loose = False
    write_score(score)
    
    board.goto(235,255)
    board.color("white")
    board.write("SPACE : ",False,"left",("Arial", 10, "bold"))
    board.goto(290,255)
    board.write("Hard Drop",False,"left",("Arial", 9, "bold"))
    board.goto(235,230)
    board.write("DOWN : ",False,"left",("Arial", 10, "bold"))
    board.goto(287,230)
    board.write("Speed Up",False,"left",("Arial", 9, "bold"))
    board.goto(235,205)
    board.write("RIGHT : ",False,"left",("Arial", 10, "bold"))
    board.goto(287,205)
    board.write("Aller à droite",False,"left",("Arial", 9, "bold"))
    board.goto(235,180)
    board.write("LEFT : ",False,"left",("Arial", 10, "bold"))
    board.goto(280,180)
    board.write("Aller à gauche",False,"left",("Arial", 9, "bold"))
    board.goto(235,155)
    board.write("UP : ",False,"left",("Arial", 10, "bold"))
    board.goto(265,155)
    board.write("Tourner",False,"left",("Arial", 9, "bold"))
    board.goto(235,-360)
    board.write("De : ",False,"left",("Arial", 9, "bold"))
    board.goto(235,-380)
    board.write("POILLY Kilyan",False,"left",("Arial", 9, "bold"))
            
def write_score(score):
    """
    Fontion qui sert à afficher le score
    en haut à droite de l'écran
    """
    
    screen.tracer(False)
    scoreT.penup()
    scoreT.setheading(0)
    scoreT.goto(308,355)
    scoreT.pendown()
    scoreT.begin_fill()
    scoreT.color("#121c33")
    for i in range(4):
        scoreT.forward(20)
        scoreT.left(90)
    scoreT.end_fill()
    scoreT.penup()
    scoreT.color("white")
    scoreT.goto(315,355)
    scoreT.write(str(score),False,"left",("Arial", 12, "bold"))

def Reset():
    """
    Fonction qui permet de recommencer une
    partie
    """
    
    Board()
    RunGame()
    
def end(x,y):
    bye()

"""
Détermination des matrices qui correspondent à chaque forme
pour chaque pièces (4 par pièce) ainsi que de leurs
couleurs associées
"""

class Barre():
    def __init__(self):
        self.shape = [[0,0,0,0,2,0,0,0,0,2,0,0,0,0,2,'#42dcf4','#7aecff','#42dcf4','#7aecff'],[0,'#42dcf4',0,0,2,0,'#7aecff',0,0,2,0,'#42dcf4',0,0,2,0,'#7aecff',0,0],[0,0,0,0,2,0,0,0,0,2,0,0,0,0,2,'#42dcf4','#7aecff','#42dcf4','#7aecff'],[0,'#42dcf4',0,0,2,0,'#7aecff',0,0,2,0,'#42dcf4',0,0,2,0,'#7aecff',0,0]]
        self.colors = ['#42dcf4','#7aecff']

class L1():
    def __init__(self):
        self.shape = [[0,0,0,0,2,0,0,0,0,2,'#5d1891',9,9,0,2,'#a742f4','#5d1891','#a742f4',0],[0,0,0,0,2,'#5d1891','#a742f4',0,0,2,'#a742f4',9,0,0,2,'#5d1891',9,0,0],[0,0,0,0,2,0,0,0,0,2,'#5d1891','#a742f4','#5d1891',0,2,9,9,'#a742f4',0],[0,0,0,0,2,9,'#5d1891',0,0,2,9,'#a742f4',0,0,2,'#a742f4','#5d1891',0,0]]
        self.colors = ['#5d1891','#a742f4']

class L2():
    def __init__(self):
        self.shape = [[0,0,0,0,2,0,0,0,0,2,9,9,'#11771c',0,2,'#1adb2d','#11771c','#1adb2d',0],[0,0,0,0,2,'#11771c',9,0,0,2,'#1adb2d',9,0,0,2,'#11771c','#1adb2d',0,0],[0,0,0,0,2,0,0,0,0,2,'#11771c','#1adb2d','#11771c',0,2,'#1adb2d',9,9,0],[0,0,0,0,2,'#11771c','#1adb2d',0,0,2,9,'#11771c',0,0,2,9,'#1adb2d',0,0]]
        self.colors = ['#11771c','#1adb2d']

class Cube():
    def __init__(self):
        self.shape = [[0,0,0,0,2,0,0,0,0,2,'#cad102','#f4fc0f',0,0,2,'#f4fc0f','#cad102',0,0],[0,0,0,0,2,0,0,0,0,2,'#cad102','#f4fc0f',0,0,2,'#f4fc0f','#cad102',0,0],[0,0,0,0,2,0,0,0,0,2,'#cad102','#f4fc0f',0,0,2,'#f4fc0f','#cad102',0,0],[0,0,0,0,2,0,0,0,0,2,'#cad102','#f4fc0f',0,0,2,'#f4fc0f','#cad102',0,0]]
        self.colors = ['#cad102','#f4fc0f']

class S():
    def __init__(self):
        self.shape = [[0,0,0,0,2,0,0,0,0,2,9,'#960000','#f91d1d',0,2,'#960000','#f91d1d',9,0],[0,0,0,0,2,'#960000',9,0,0,2,'#f91d1d','#960000',0,0,2,9,'#f91d1d',0,0],[0,0,0,0,2,0,0,0,0,2,9,'#960000','#f91d1d',0,2,'#960000','#f91d1d',9,0],[0,0,0,0,2,'#960000',9,0,0,2,'#f91d1d','#960000',0,0,2,9,'#f91d1d',0,0]]
        self.colors = ['#960000','#f91d1d']

class T():
    def __init__(self):
        self.shape = [[0,0,0,0,2,0,0,0,0,2,9,'#010677',9,0,2,'#010677','#000cff','#010677',0],[0,0,0,0,2,'#010677',9,0,0,2,'#000cff','#010677',0,0,2,'#010677',9,0,0],[0,0,0,0,2,0,0,0,0,2,'#010677','#000cff','#010677',0,2,9,'#010677',9,0],[0,0,0,0,2,9,'#010677',0,0,2,'#010677','#000cff',0,0,2,9,'#010677',0,0]]
        self.colors = ['#010677','#000cff']

class Z():
    def __init__(self):
        self.shape = [[0,0,0,0,2,0,0,0,0,2,'#a36400','#ff9d00',9,0,2,9,'#a36400','#ff9d00',0],[0,0,0,0,2,9,'#a36400',0,0,2,'#a36400','#ff9d00',0,0,2,'#ff9d00',9,0,0],[0,0,0,0,2,0,0,0,0,2,'#a36400','#ff9d00',9,0,2,9,'#a36400','#ff9d00',0],[0,0,0,0,2,9,'#a36400',0,0,2,'#a36400','#ff9d00',0,0,2,'#ff9d00',9,0,0]]
        self.colors = ['#a36400','#ff9d00']

def remplCase(x,y,colorp):
    """
    Fonction qui dessine un carré pour la pièce
    en cours
    """
    
    draw.resizemode("user")
    draw.pensize(3)
    draw.color("#000000")
    draw.penup()
    draw.goto(x,y)
    draw.pendown()
    draw.begin_fill()
    draw.setheading(0)
    for i in range(4):
        draw.forward(30)
        draw.right(90)
    draw.color(colorp)
    draw.end_fill()

def remplCaseGrid(x,y,colorp):
    """
    Fonction qui sert à redessiner les carrés
    de la grille lorsque qu'il est nécessaire
    (en cas de ligne complète par exemple
    """
    
    grid.resizemode("user")
    grid.pensize(3)
    grid.color("#000000")
    grid.penup()
    grid.goto(x,y)
    grid.pendown()
    grid.begin_fill()
    grid.setheading(0)
    for i in range(4):
        grid.forward(30)
        grid.right(90)
    grid.color(colorp)
    grid.end_fill()

def TetrisBrick():
    """
    Fonction qui choisit aléatoirement une pièce
    """
    
    ListBrick = [Barre(),L1(),L2(),Cube(),S(),T(),Z()]
    nb = randint(0,6)

    return ListBrick[nb]

def CheckLine(ListGrid):
    """
    Fonction qui vérifie si une ou plusieurs lignes
    sont complètes
    """
    
    global score
    for i in range(len(ListGrid)-1) :
        if 0 not in ListGrid[i]:
            score += 1
            write_score(score)
            ListGrid[i] = [0]*20

            for k in reversed(range(i)):
                for j in reversed(range(len(ListGrid[k]))):
                    if type(ListGrid[k][j]) is str :
                        ListGrid[k+1][j] = ListGrid[k][j]
                        ListGrid[k][j] = 0
    grid.clear()
    drawGrid(ListGrid)            

def DisplayResult(score):
    """
    Fonction qui affiche la fenêtre de fin qui contient
    le score du joueur ainsi qu'une proposition de
    rejouer
    """
    
    screen.tracer(False)
    board.penup()
    board.goto(-195, 195)
    board.color("white")
    board.pendown()
    board.begin_fill()
    board.setheading(0)
    board.forward(240)
    board.right(90)
    board.forward(180)
    board.right(90)
    board.forward(240)
    board.right(90)
    board.forward(180)
    board.color("#121c33")
    board.end_fill()
    board.penup()
    board.pensize(1)
    board.color("white")
    board.goto(-75, 155)
    board.write("TERMINÉ !",False,"center",("Arial", 20, "bold"))
    board.goto(-85, 125)
    board.write("SCORE :",False,"center",("Arial", 13, "bold"))
    board.setheading(0)
    board.forward(50)
    board.write(str(score),False,"center",("Arial", 13, "bold"))
    board.goto(-75, 90)
    board.write("Voulez-vous rejouer ?",False,"center",("Arial", 13, "bold"))
    
    board.penup()
    board.goto(-165, 65)
    board.setheading(0)
    board.pendown()
    screen.tracer(False)

    for j in range(0,2):
        board.forward(j*120)
        board.pendown()
        for i in range(2):
            board.forward(60)
            board.right(90)
            board.forward(25)
            board.right(90)
        board.penup()
        if j == 0 :
            board.right(45)
            board.forward(30)
            board.write("OUI",False,"left",("Arial", 8, "bold"))
            board.backward(30)
            board.left(45)
        if j == 1 :
            board.right(45)
            board.forward(30)
            board.write("NON",False,"left",("Arial", 8, "bold"))
            board.backward(30)
            board.left(45)
    screen.onscreenclick(checkClick)
            
def checkClick(x,y):
    """
    Fonction qui détermine le choix du joueur en fonction de
    où il clique lorsqu'il lui est demandé s'il veut rejouer
    """
    
    if x >= -165 and x <= -105 and y >= 40 and y <= 65:
        Reset()
    elif x >= -45 and x <= 15 and y >= 40 and y <= 65:
        bye()

def move_right():
    """
    Fonction dui sert à déplacer la pièce vers la droite
    """
    
    global brick
    global EntreList
    global ListGrid
    
    for j in reversed(range(len(EntreList))):
            for k in reversed(range(len(EntreList[j]))):
                if (EntreList[j][k] in brick.colors or EntreList[j][k] == 9) and k+1 <= (len(EntreList[j])-1) and ListGrid[j][k+1] == 0 and EntreList[j][k+1] == 0:
                    if ListGrid[j][k+1] == 0:
                        EntreList[j][k+1] = EntreList[j][k]
                        EntreList[j][k] = 0
      
def move_left():
    """
    Fonction dui sert à déplacer la pièce vers la gauche
    """
    
    global brick
    global EntreList
    global ListGrid

    for j in reversed(range(len(EntreList))): 
            for k in range(len(EntreList[j])):
                if (EntreList[j][k] in brick.colors or EntreList[j][k] == 9) and k-1 >= 0 and ListGrid[j][k-1] == 0 and EntreList[j][k-1] == 0:
                    EntreList[j][k-1] = EntreList[j][k]
                    EntreList[j][k] = 0

def changeAngle():
    """
    Fonction qui modifie l'angle de la pièce
    """
    
    global angle
    global EntreList

    posX = 0
    posY = 0

    angle += 1

    if angle >= 4:
        angle = 0

    for j in reversed(range(len(EntreList))):
        for k in range(len(EntreList[j])):
            if EntreList[j][k] in brick.colors:
                if angle == 0 or angle == 2:
                    X = k
                else:
                    X = k-1
                posY = j-2
                break
    
    EntreList = [[0]* 20 for i in range(31)]
    EntreList[30] = [1]*20
    posX = X
    
    for i in brick.shape[angle]:
        if i == 0:
            posX += 1
        elif i == 2:
            posX = X
            posY += 1
        else:
            EntreList[posY][posX] = brick.shape[angle][brick.shape[angle].index(i)]
            posX += 1

    drawPiece(EntreList,brick)
    
def speedUp():
    """
    Fonction qui accelère la chute de la pièce
    """
    
    global delais
    delais = 0.04
def speedDown():
    """
    Fonction qui restaure la chute par défaut
    """
    
    global delais
    delais = 0.1
def hardDrop():
    """
    Fonction qui fait descndre la pièce très
    rapidement si la barre d'espace est pressée
    """
    
    global delais
    delais = 0.004
    
def drawGrid(ListGrid):
    """
    Fonction qui dessine la grille (qui comprends
    toutes les pièces une fois qu'elles finissent
    leur chute)
    """
    
    x = -375
    current_x = x
    current_y = 518
    screen.tracer(False)
    for i in ListGrid:
        for j in ListGrid[ListGrid.index(i)]:
            if j == 0:
                current_x += 30
            if type(j) is str :
                remplCaseGrid(current_x,current_y,j)
                current_x += 30
        current_y -= 30
        current_x = x

    screen.update()

def drawPiece(EntreList,brick):
    """
    Fonction qui dessine la pièce le long de
    sa chute
    """
    
    global delais
    
    screen.tracer(3)
    x = -375
    current_x = x
    current_y = 518
    draw.clear()
    count = 0
    screen.tracer(False)
    for i in EntreList:
        for j in EntreList[EntreList.index(i)]:
            if j == 0 or j == 9:
                current_x += 30
            if j in brick.colors :
                remplCase(current_x,current_y,j)
                current_x += 30
                count +=1
            if count == 4:
                count = 0
                sleep(delais)
        current_y -= 30
        current_x = x

def addPieceToGrid(EntreList,ListGrid):
    """
    Fonction qui ajoute la pièce à la grille une
    fois sa chute terminée
    """
    
    for j in range(len(EntreList)):
        for k in range(len(EntreList[j])):
            if type(EntreList[j][k]) is str:
                ListGrid[j][k] = EntreList[j][k]
    return ListGrid

def RunGame():
    """
    Fonction qui contient l'ensemble du jeu
    """
    
    global EntreList
    global angle
    global brick
    global delais
    
    ListGrid = [[0]* 20 for i in range(31)]
    ListGrid[30] = [1]*20
    NewListGrid = deepcopy(ListGrid)
    EntreList = deepcopy(ListGrid)
    Loose = False

    ligne = 0 #reviens à 0 dans le while
    colonne = 8 #reviens à 8 dans le while

    GridY = 0 #Reviens à 0 dans le while
    GridX = 8 #reviens à 8 dans le while
    count = 0


    while Loose == False :
        
        angle = 0
        delais = 0.1
        brick = TetrisBrick()
        GridY = ligne #Reviens à 0 dans le while
        GridX = colonne #reviens à 8 dans le while
        Arrived = False

        for i in brick.shape[angle]:
            if i == 0:
                GridX += 1
            elif i == 2:
                GridX = colonne
                GridY += 1
            else:
                NewListGrid[GridY][GridX] = brick.shape[angle][brick.shape[angle].index(i)]
                GridX += 1

        while Arrived == False:
            screen.onkey(changeAngle, "Up")
            screen.onkeypress(speedUp, "Down")
            screen.onkey(hardDrop, "space")
            screen.onkeypress(move_right, "Right")
            screen.onkeypress(move_left, "Left")
            screen.onkeyrelease(speedDown, "Down")
            
            count = 0
            for j in reversed(range(len(NewListGrid))):
                for k in range(len(NewListGrid[j])):
                    if (NewListGrid[j][k] in brick.colors and ListGrid[j+1][k] == 0):
                        NewListGrid[j+1][k] = NewListGrid[j][k]
                        NewListGrid[j][k] = 0
                        count += 1
                    elif NewListGrid[j][k] == 9 and ListGrid[j+1][k] == 0:
                        NewListGrid[j+1][k] = NewListGrid[j][k]
                        NewListGrid[j][k] = 0
                        
            if count == 4:
                EntreList = deepcopy(NewListGrid)
            else:
                Arrived = True
            
            drawPiece(EntreList,brick)
            sleep(delais)
            screen.update()
            NewListGrid = deepcopy(EntreList)
            screen.listen()
      
        ListGrid = addPieceToGrid(EntreList,ListGrid)
        NewListGrid = [[0]* 20 for i in range(31)]
        NewListGrid[30] = [1]*20
        drawGrid(ListGrid)
        CheckLine(ListGrid)

        if ListGrid[4] != [0]*20:
            DisplayResult(score)
            Loose = True
        

        
ht()
screen = Screen()
screen.bgcolor("black")
screen.setup(760,820)
screensize(760,820)
speed(0)
screen.tracer(False)

board = Turtle()
board.ht()
draw = Turtle()
draw.ht()
Line = Turtle()
Line.ht()
scoreT = Turtle()
scoreT.ht()
grid = Turtle()
grid.ht()

brick = TetrisBrick()
score = 0
angle = 0
delais = 0.3

ListGrid = [[0]* 20 for i in range(31)]
ListGrid[30] = [1]*20
NewListGrid = deepcopy(ListGrid)
EntreList = deepcopy(ListGrid)
    
Board()
RunGame()

