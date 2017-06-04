#!/usr/bin/env python3
#-*-coding:UTF-8-*-


def CinDico(caractere, dictionnaire):
    
    test = -1
    for i in range(0, len(dictionnaire)):
        if caractere == dictionnaire[i][0]:
            test = i
    return test

def startDecompress(fileName):
    """

    """
    lines=LectureFichier(fileName)
    fileOut=fileName.split(".")[0]+".txt"
    Decompress(lines,fileOut)

def LectureFichier(chemin):

    fichier = open(chemin, 'rb')

    ligne = fichier.readlines()
    
    binary = ""
    print(ligne)
    print("\n")
    n = len(ligne)
    for i in range(1, n-1):
        ligne[0] = ligne[0] + ligne[i]
    print(ligne)
    print("\n")
    ligne = [ligne[0], ligne[-1]]
    print(ligne) 
    print("\n")
    
    for i in range(0, len(ligne[1])):
        bit9 = str(bin(ligne[1][i]))
        n = len(bit9)-2
        
        zero = ""
        for k in range(0, 8-n):
            zero = zero + "0"
        bit9 = zero + bit9[2:]
        
        for j in range(0, len(bit9)) :
            carac = str(bin(ligne[0][8*i + j]))
            n = len(carac) - 2
            zero = ""
            for k in range(0, 8-n):
                zero = zero + "0"
            carac = "0b" + zero + carac[2:]
            binary = binary + "0b" + bit9[j] + carac[2:] + " "

    ligne = binary.split("0b")
    ligne.remove('')
    print(ligne)
    print("\n")
    fichier.close()
    return ligne


def Decompress(caracteres,fileOut):

    resultat = open("fileOut", 'w')

    dictionnaire = []

    resultat.write(chr(int(caracteres[0], 2)))
    w = chr(int(caracteres[0], 2))

    for i in range(1, len(caracteres)):
        presence = CinDico(int(caracteres[i], 2), dictionnaire)
        test_code = int(caracteres[i], 2)
        if test_code > 255 and  presence != -1 :
            entree = dictionnaire[presence][1]

        elif test_code > 255 and presence == -1 :
            entree = w + w[0]
        else :
            entree = chr(test_code)

        resultat.write(entree)
        
        if len(dictionnaire) == 256 :
            dictionnaire = []
            
        try :
            dictionnaire.append([dictionnaire[-1][0] + 1, w + entree[0]])
        except IndexError :
            dictionnaire.append([256, w + entree[0]])
        
        w = entree

    print(dictionnaire)
    resultat.close()
    return "Opération Réussie !"
