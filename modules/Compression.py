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
        compressLZW(datas,fileOut)
    else:
        print('Error')

def compressLZW(String,fileName):
    """
    Fonction qui permet de compresser une chaine de caractère en
    suivant l'algo Lempel-Ziv-Welch.

    :param: une chaine de caractère
    :return output: la chaine compressé
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
            print(nineBits)
            for i in range(0,len(nineBits),8):
                nineBytes=bytes([int(nineBits[i:i+8],2)])
                archive.write(nineBytes)
            archive.close()
    except IOError as error:
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
