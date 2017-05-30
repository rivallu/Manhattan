#!/usr/bin/env python3
#-*-coding:UTF-8-*-


def CinDico(caractere, dictionnaire):
    test = False
    for i in range(0, len(dictionnaire)):
        if caractere == dictionnaire[i][0]:
            test = True
    return test
    

def Decompress():
    fichier = open("C://Users//matth//Documents//ENSIBS//Programmation Objet//Manhattan//test//archive.lzw", 'rb')
    resultat = open("resultat.txt", 'w')

    ligne = fichier.readlines()
    
    print(ligne)
    
    binary = ""
    
    for i in range(0, len(ligne[0])):
        binary = binary + str(bin(int(ligne[0][i], 16)))
    
    caracteres = []
    dictionnaire = []
    
    for i in range(0, len(binary), 10):
        caracteres.append(ligne[0][i:i+10])

    resultat.write(char(caracteres[0]))
    w = chr(int(caracteres[0], 2))

    for i in range(1, len(caracteres)):
        if int(caracteres[i], 2) > 255 and CinDico(int(caracteres[i], 2), dictionnaire) :
            for i in range(0, len(dictionnaire)) :
                if dictionnaire[i][0] == int(caracteres[i], 2) :
                    entree = dictionnaire[i][1]
                    break
        elif int(caracteres[i], 2) > 255 and CinDico(int(caracteres[i], 2), dictionnaire) == False :
            entree = w + w[0]
        else :
            entree = chr(int(caracteres[i], 2))
        resultat.write(entree)
        dictionnaire.append([dictionnaire[-1][0] + 1, w + entree[0]])
        w = entree
    
    fichier.close()
    resultat.close()
    
    
    
    #exctraction du caractère
    #w = c
    #dictionnaire = []

    #while c != '' :
        #if c > 255 and CinDico(c, dictionnaire) :
            #entree = 
            
    dictionnaire = []
    print(caracteres)