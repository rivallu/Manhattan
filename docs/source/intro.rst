Introduction
============

Bienvenue dans la documentation du projet Manhattan.
Le but de ce projet est de pouvoir compresser un fichier et de le décompresser.
Les algorythmes supportés par ce programme sont :

- Lempel-Ziv-Welch.


Par défaut le fichier compressé se nomme ``archive`` suivi de l'extention en fonction de l'algothime utilisé.

Fonctionnement
--------------

Manhattan -h permet d'afficher l'aide.
l'option -f doit être placé à la fin de toutes les options car l'option -f attend
un nom de fichier après. L'option -o doit être placée à part pour les mêmes raisons que pour l'option -f/

exemple pour la compression:
::
        python3 Manhattan -clf test/latin.txt


        python3 Manhattan -xlf test/latin.txt -o latin

exemple de décompression:
::
        python3 Manhattan -xlf test/archive.lzw


Choix
-----
Pour la compression nous avons fait le choix de coder sur 9 bits, puis de couper
le bit de poids fort et de le mettre à part. 

A la fin de la compression, tous les bits de poids fort sont mis
ensemble puis traduits en hexadécimal pour éviter de prendre trop de place. 

Pour déterminer où se trouve les bits de poids fort, nous avons décidé d'insérer deux caractères ``0A``.


Format du fichier d'entrée
--------------------------

Le fichier fourni à l'algorithme doit avoir les propriétés suivantes :

- Format .txt;
- Composé de caractères appartenant à l'ASCII étendu uniquement;
- Ne pas comporter de saut de ligne (soit deux "\n" à la suite);



Améliorations
-------------
- Rajouter le pourcentage de compression de deux fichiers
- Rajouter des algorithmes supplémentaires
- Rajout de l'option -o pour la décompression
- Changer le séparateur entre le texte et les 9èmes bits afin de permettre l'utilisation de textes avec saut de ligne.
- Spliter la fonction compressLZW en sous fonctions plus simples.
