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
    Decompress(lines)

def LectureFichier(chemin):

    fichier = open(chemin, 'rb')

    ligne = fichier.readlines()

    binary = ""

    for i in range(0, len(ligne[0])):
        binary = binary + str(bin(ligne[0][i])) + " "

    ligne = binary.split("0b")
    ligne.remove('')

    fichier.close()
    return ligne


def Decompress(caracteres):

    resultat = open("C://Users//matth//Documents//ENSIBS//Programmation Objet//Manhattan//resultat.txt", 'w')
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

        try :
            dictionnaire.append([dictionnaire[-1][0] + 1, w + entree[0]])
        except IndexError :
            dictionnaire.append([256, w + entree[0]])

        w = entree

    print(dictionnaire)
    resultat.close()
    return "Opération Réussie !"
