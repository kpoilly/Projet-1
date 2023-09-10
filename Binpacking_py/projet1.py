import sys
import time

file = sys.argv[1]

def binPacking(file):
    f = open(file, 'r')
    liste = []
    for line in f:
        liste.append(int(line.strip()))

    cap = liste.pop(0) #Capacité des boîtes

    print("Capacité des boites : ",cap)
    print("Nombre d'objets : ",len(liste))
    print("Poids des objets : ", end="")

    for elem in liste: #Print des éléments du fichiers txt.
        print(elem,end="")
        if liste.index(elem) != len(liste)-1:
            print(", ", end="")
            
    print("\n"+"Résolution...")
    
    ListeBoites = [] #Liste qui servira à stocker les différentes boîtes remplies
    ListeBoites = fillBin(liste, cap, ListeBoites)
    printSoluce(ListeBoites)

def fillBin(liste, cap, ListeBoites):
    """
    Fonction qui remplie les boîtes selon leur cap maximum
    """
    currentBoite = [] #Boîte actuelle
    currentBoite.append(liste.pop(liste.index(liste[0]))) #Ajout du 1er elem de la liste d'elems
    full = False
    seek = cap-sum(currentBoite) #Element recherché dans la liste
    
    while not full :
        """
        Ici, on remplie la boîte actuelle, la façon de procédé est la suivante :
        On recherche le "seek" qui est en fait cap - la somme des éléments de la boîte
        (soit le plus gros élément possible pour remplir la boîte)
        Si on le trouve, on l'ajoute et on calcul un nouveau seek, sinon, on recherche
        le seek-1, et ainsi de suite.
        """
        if sum(currentBoite) < cap :
            for item in liste:
                if item == seek:
                    currentBoite.append(liste.pop(liste.index(item)))
                    seek = cap-sum(currentBoite)
                    
            seek -= 1
            if len(liste) == 0 or seek < min(liste):
                full = True

    ListeBoites.append(currentBoite) #Une fois remplie, on ajoute la boîte à la liste des boîtes.
    
    if len(liste) != 0: #Si il reste des éléments qui n'ont pas de boîte, on remplie une nouvelle boîte.
        ListeBoites = fillBin(liste, cap, ListeBoites)
        
    return ListeBoites

def printSoluce(ListeBoites):
    """
    Fonction qui print la solution.
    """
    print("Solution à",len(ListeBoites),"boites trouvée...")
    print("Meilleure solution :")
    print(len(ListeBoites),"boites")

    for i in range(len(ListeBoites)):
        print("Boite",i+1,":",*ListeBoites[i],"; total :",sum(ListeBoites[i]))


start = time.time()
binPacking(file)
end = time.time()
print("Temps de résolution : %.3f s" % (end - start))
