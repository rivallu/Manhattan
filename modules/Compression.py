#!/usr/bin/env python3
#-*-coding:UTF-8-*-


def genDict():
    """
    Fonction qui génère un dictionnaire pour permettre la compression.

    :return dico: le dictionnaire
    """
    dico={}
    for i in range(0,256):
        dico.update({chr(i):i})
    return dico

def compress(fileIn,fileOut,algo):
    """
    Fonction générique qui fait les appels au différentes fonctions pour compresser
    en fonction de l'algo donnée.

    :param fileIn: Le fichier à compresser
    :param fileOut: le fichier de sortie
    :param algo: l'algo utilisé pour la compression.
    """
    if algo=="lzw":
        datas=openFileToCompress(fileIn)
        writteFile(compressLZW(datas),fileOut)
    else:
        print('Error')

def compressLZW(String):
    """
    Fonction qui permet de compresser une chaine de caractère en
    suivant l'algo Lempel-Ziv-Welch.

    :param: une chaine de caractère
    :return output: la chaine compressé
    """
    print(String)
    output=''
    dico=genDict()
    w=''
    for letter in String:
        element='{}{}'.format(w,letter)
        if element in dico:
            w=element
        else:
            dico.update({element:len(dico)})
            binary="{0:b}".format(dico.get(w))
            # print('{} {}'.format(letter,binary))
            binary=paddin(binary)
            output+=binary
            w=letter;
    return output

def paddin(binary):
    """
    Fonction qui permet d'ajouter du paddin à un nombre binaire. le nombre renvoyé
    est sur 9 bits.

    :param: un nombre binaire
    :return binary: le même nombre binaire mais sur 9 bits
    """
    while(len(binary)<10):
        binary="{0:b}".format(0)+binary
    return binary

def writteFile(bytesString,fileName):
    """
    Fonction qui permet d'écrire le contenu compresser dans un fichier binaire.

    :param: la chaine compresser en binaire
    :raise IOError: retourne le code d'erreur de la classe IO.
    """
    try:
        with open(fileName,'wb+') as archive:
            for h in range(0,len(bytesString),8):
                hexString=bytesString[h:h+8]
                hexInt=int(hexString,2)
                archive.write(bytes([hexInt]))
            archive.close()
    except IOError as error:
        print('writteFile')
        raise error

def openFileToCompress(fileName):
    """
    Fonctio qui va lire le fichier passé en paramètre et va retoruner tout son
    contenu.

    :param: le nom du fichier à ouvrir
    :raise IOError:  les erreurs éventuelle sur la lecture du fichier.
    """
    try:
        with open(fileName,'r') as f:
            lines=f.readlines()
            lines=" ".join(lines)
            f.close()
            return lines
    except IOError as error:
        print('openFileToCompress')
        raise error

if __name__ == '__main__':
    # assert(paddin('000001')=='0000000001')
    # assert(paddin('000001')!='00000001')
    # f= open("../test/test",'r')
    # line=f.read()
    # f.close
    # print(compress("TOBEORNOTTOBEORTOBEORNOT"))
    print(compress("TOBEORNOTTOBEORTOBEORNOT"))
    # writteFile(compress(line))
