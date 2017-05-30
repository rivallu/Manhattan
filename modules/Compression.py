#!/usr/bin/env python3
#-*-coding:UTF-8-*-


def genDict():
    """
    Fonction qui génère un dictionnaire
    :return: le dictionnaire
    """
    dico={}
    for i in range(0,256):
        dico.update({chr(i):i})
    return dico

def compress(String):
    """
        Fonction qui permet de compresser une chaine de caractère en
        suivant l'algo Lempel-Ziv-Welch.
        :param: une chaine de caractère
        :return: la chaine compressé
    """
    output=b''
    dico=genDict()
    w=''
    for letter in String:
        element='{}{}'.format(w,letter)
        if element in dico:
            w=element
        else:
            dico.update({element:len(dico)})
            output+=str.encode(bin(dico.get(w)))
            w=letter;
    return output


if __name__ == '__main__':
    print(compress("TOBEORNOTTOBEORTOBEORNOT"))
