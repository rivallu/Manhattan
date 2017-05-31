#!/usr/bin/env python3
#-*-coding:UTF-8-*-

from modules import Compression
from modules import Decompression
import argparse
import time
import datetime


def parse_args():
    """
    Fonction qui permet de gérer les arguments passé en paramètre.
    """

    parser = argparse.ArgumentParser(description='... saves many files together...')
    parser.add_argument('--extract', '-x',
                        action='store_true',
                        help='extract files from an archive')
    parser.add_argument('--verbose', '-v',
                        action='store_true',
                        help='verbosely list files processed')
    parser.add_argument('--create', '-c',
                        action='store_true',
                        help='verbosely list files processed')
    parser.add_argument('--lzw', '-l',
                        action='store_true',
                        help='compress using Lempel-Ziv-Welch algo')
    parser.add_argument('--file', '-f',
                        # dest='file', -- only needed if the long form isn't first
                        help='use archive file or device ARCHIVE')
    parser.add_argument('--output', '-o',
                        # dest='file', -- only needed if the long form isn't first
                        help='file name of the archive file')
    return parser.parse_args()


def convertToH(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    time="{}:{}:{}".format(int(h),int(m),int(s))
    return time



arg=parse_args()
tps1 = time.time()
if arg.create:
    print('Début de la compression')
    if arg.output is not None:
        fileName=arg.output+'.lzw'
    else:
        fileName='archive.lzw'
    try:
        Compression.compress(arg.file,fileName,"lzw")
    except Exception as error:
        print(error)
elif arg.extract:
    print('Début de la décompression')
tps2 = time.time()
totalTime=tps2-tps1
totalTime=convertToH(totalTime)
print(totalTime)
