#!/usr/bin/python
import sys
import argparse
import numpy as np
from itertools import combinations

def main(filename, prefix):
    numberlist = np.loadtxt("input.txt",dtype=int)
    comblist = combinations(numberlist,2)
    comb = next(comblist)
    while comb[0]+comb[1] != 2020:
        comb = next(comblist)
    print("Oggi ho mangiato ", comb[0]*comb[1], " torte")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Whatever this is going to do")
    parser.add_argument("--filename", type = str, default="input.txt", help = "The name of the file")
    parser.add_argument("--prefix", type=str,default=None, help="Prefix for all output filenames")


    args = parser.parse_args()
    sys.exit(main(args.filename,args.prefix))
