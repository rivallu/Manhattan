#!/usr/bin/env python3
#-*-coding:UTF-8-*-


def genDict():
    """
    Fonction qui génère un dictionnaire pour permettre la compression.

    :return dico: le dictionnaire contenant les caractères ASCII étendu et leur code en décimal.
    """
    dico={}
    for i in range(0,256):
        dico.update({chr(i):i})
    return dico

def compress(fileIn,fileOut,algo):
    """
    Fonction générique qui fait les appels aux différentes fonctions pour compresser selon l'algorithme sélectionné.

    :param fileIn: Le fichier à compresser.
    :param fileOut: le fichier de sortie.
    :param algo: l'algorithme utilisé pour la compression.
    """
    if algo=="lzw":
        datas=openFileToCompress(fileIn)
        compressLZW(datas,fileOut)
    else:
        print('Error')

def compressLZW(String,fileName):
    """
    Fonction qui permet de compresser une chaine de caractères en
    suivant l'algorithme Lempel-Ziv-Welch.

    :param: Chaîne de caractères devant être compressée. A fournir avec le type string.
    :param fileName: Le chemin d'accès du fichier à compresser.
    """
    output=''
    dico=genDict()
    nineBits=''
    w=''
    try:
        with open(fileName,'wb+') as archive:
            for letter in String:
                element='{}{}'.format(w,letter)
                if len(dico)==512:
                    dico=genDict()
                if element in dico:
                    w=element
                else:
                    dico.update({element:len(dico)})
                    binary="{0:b}".format(dico.get(w))
                    if len(binary)==9:
                        nineBits+=binary[0]
                        binary=binary[1:]
                    else:
                        nineBits+='0'
                    hexInt=int(binary,2)
                    w=letter;
                    archive.write(bytes([hexInt]))
            for i in range(0,len(nineBits)%8):
                nineBits=nineBits+("{0:b}".format(0))*(8 - len(nineBits)%8)
            archive.write(b'\n')
            archive.write(b'\n')
            for i in range(0,len(nineBits),8):
                nineBytes=bytes([int(nineBits[i:i+8],2)])
                archive.write(nineBytes)
            archive.close()
    except IOError as error:
        raise error

def openFileToCompress(fileName):
    """
    Fonction lisant le fichier passé en paramètre et retournant son contenu.

    :param fileName: Le chemin d'accès du fichier à lire.
    :raise IOError:  Les erreurs éventuelles sur la lecture du fichier.. Les erreurs
    sont renvoyé dans Manhattan.py où les erreurs seront géré (affiché à l'utilisateur).
    """
    try:
        with open(fileName,'r') as f:
            lines=f.readlines()
            lines=" ".join(lines)
            f.close()
            return lines
    except IOError as error:
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
