#!/usr/bin/env python3
#-*-coding:UTF-8-*-


class Compression:

    def compress(String):
        """
            Fonction qui permet de compresser une chaine de caractère en
            suivant l'algo Lempel-Ziv-Welch.
            :param: une chaine de caractère
            :return: la chaine compressé
        """
        output=
        dico={}
        w=null
        for letter in String:
            element='{}{}'.format(w,letter)
            if dico.has_key(element):
                w=element
            else:
                dico.update(element:??)
                output+=w
                w=letter;
        print(output)
        return output
