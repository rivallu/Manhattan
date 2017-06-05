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
    n = len(ligne)
    ninebit = ""
    sauv = 0
    for i in range(0, n):
        if ligne[i] == b'\n' :
            sauv = i

    for i in range(1, sauv):
        ligne[0] = ligne[0] + ligne[i]

    for i in range(sauv+1, n):
        ligne[sauv] = ligne[sauv] + ligne[i]

    ligne = [ligne[0], ligne[sauv][1:]]
    for i in range(0, len(ligne[1])):
        bit9 = str(bin(ligne[1][i]))
        n = len(bit9) - 2

        zero = ""
        for k in range(0, 8-n):
            zero = zero + "0"
        bit9 = zero + bit9[2:]

        ninebit = ninebit + bit9

        for j in range(0, len(bit9)) :
            try :
                carac = str(bin(ligne[0][8*i + j]))
            except IndexError :
                break

            n = len(carac) - 2
            zero = ""
            for k in range(0, 8-n):
                zero = zero + "0"
            carac = "0b" + zero + carac[2:]
            binary = binary + "0b" + bit9[j] + carac[2:] + " "

    ligne = binary.split("0b")
    ligne.remove('')
    fichier.close()
    return ligne


def Decompress(caracteres,fileOut):

    resultat = open(fileOut, 'w')

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

        if len(dictionnaire) == 256 :
            dictionnaire = []

        w = entree

    resultat.close()
    return "Opération Réussie !"