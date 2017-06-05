#!/usr/bin/env python3
#-*-coding:UTF-8-*-


def CinDico(caractere, dictionnaire):
    
    """
    Fonction permettant de détecter la présence d'un code dans le dictionnaire construit par Decompress.
    
    :param caractere: Paramètre correspondant au code d'un caractère ou d'une suite de caractères compressé.
    :param dictionnaire: Liste correspondant au dictionnaire en cours d'utilisation et construit par Decompress()
    
    :return test: Variable de type Integer ayant pour valeur -1 si le code ne se trouve pas dans le dictionnaire entrée en paramètre ou la position du code dans le dictionnaire en cas de détection. Cela permet à Decompress de récupérer la suite de caractères correspondante.
    """
    
    test = -1
    for i in range(0, len(dictionnaire)):
        if caractere == dictionnaire[i][0]:
            test = i
    return test

def startDecompress(fileName):
    """
    Fonction générique permettant de décompresser suivant l'algorithme de compression utilisé.
    
    :param fileName: Chemin d'accès de l'archive dont on souhaite la décompression.
    """
    lines=LectureFichier(fileName)
    fileOut=fileName.split(".")[0]+".txt"
    Decompress(lines,fileOut)

def LectureFichier(chemin):
    
    """
    Fonction permettant de lire l'archive et de produire une liste formatée pour la décompression par la fonction Decompress().
    
    LectureFichier produit d'abord une liste contenant chaque ligne de l'archive compressée.
    
    La compression ayant ajouté 2 "\n" dans l'archive, LectureFichier cherche donc un élément de la liste correspondant à "b'\n'" afin de collecter tout ce qui se toruve avant comme étant du texte à décoder et tout ce qui se trouve après comme étant le bit de poids fort manquant à chaque caractère.
    
    Par la suite, LectureFichier lit chaque bit de poids fort et l'ajoute au code du caractère auquel il devrait appartenir.
    
    Enfin, chaque code est casté en string puis le "0b" restant suite au cast est retiré afin de ne garder qu'une suite de bit.
    
    Enfin, la fonction retourne la liste correctement formatée et exploitable par Decompress()
    
    :param chemin: Paramètre contenant le chemin d'accès de l'archive à décompresser.
    
    :raise IndexError: Afin de coder les 9ème bits en hexadecimal, il a fallu ajouter des 0 non significatifs à la fin de la liste des 9ème bits. En effet, nous devions posséder une liste de 9ème bits divisible par 8 pour coder en hexadécimal d'où l'ajout de zéro. Cela entraîne ici une erreur IndexError étant donné qu'il n'existe pas de code en hexadécimal pour les 9ème bits ajoutés artificiellement. On sort alors de la boucle for en provoquant un break une fois cette erreur rencontrée (qui correspondra donc au premier 9ème bits non significatifs).
    
    :return ligne: Liste formatée des codes de caractères sur 9 bits prête à être interprêtée par Decompress()
    """
    
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
    
    """
    Decompress est la fonction servant à décoder un texte compressé en suivant la méthode de l'algorithme LZW.
    
    Elle s'appuie sur la fonction LectureFichier afin de recevoir une liste correctement formatée pour la décompression.
    
    :param caracteres: Il s'agit d'une liste dont chaque élément correspond au code ASCII ou du dictionnaire d'un caractère ou d'une suite de caractère compressé. Ce code doit être exprimé en bit, type string sans le 0b ajouté par le type bytes. LectureFichier() peut fournir une telle liste formatée à partir d'un fichier texte.
    :param fileOut: Paramètre contenant le chemin d'accès souhaité par l'utilisateur pour écriture du fichier décompressé.
    
    :raise IndexError: Lors du premier ajout au dictionnaire, la liste est vide. Or, dans le try, nous essayons de récupérer le dernier indice du code ajouté au dictionnaire. Cela générère une erreur IndexError qui est gérée dans le except. En effet, dans ce cas, nous ajoutons au dictionnaire le code avec pour indice 256 ce qui permet de l'initialiser et de ne plus rencontrer l'erreur par la suite.
    """
    
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