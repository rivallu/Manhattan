Introduction
============

Bienvenu dans la documentation du projet Manhattan.
Le but de ce projet est de pouvoir compresser un fichier et de le décompresser.
Les algorythmes supportés par ce programme sont :

- Lempel-Ziv-Welch.


Par défaut le fichier compresser se nomme ``archive`` suivi de l'extention en fonction de l'algothime utilisé.

Fonctionnement
--------------

Manhattan -h permet d'afficher l'aide.
l'option -f doit être placé à la fin de toute les options car l'option -f attend
un nom de fichier après. L'option -o doit être placé à part pour les même raison que pour l'option -f/

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
le bit de poid fort et de le mettre à part. A la fin de la compression tout les bits de poid fort sont mit
ensemble puis traduit en hexadécimal pour éviter de prendre trop de place. Pour déterminer où se trouve les bits de poid fort
nous avons décider d'insérer deux caractères ``0a``.




Amélioration
------------
- Rajouter le pourcentage de compression de deux fichiers
- Rajouter des algo supplémentaire
- rajout option -o pour la décompression
- changer le séparateur entre le texte et les 9èmes bits.
- spliter la fonction compressLZW en sous fonction plus simple
