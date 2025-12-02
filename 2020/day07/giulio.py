#!/usr/bin/python
import sys
import argparse

def count_ex_1(bagDict, bagToCheck, checkedBags=[]):
    
    totalNumber = 0
    for key,value in bagDict.items():
        if value[0] == "":
            pass
        else:
            for bagInside in value:
                tmpBag = bagInside.split(" ")
                compareBag = tmpBag[1] + " " + tmpBag[2]
                if compareBag == bagToCheck:
                    if key not in checkedBags:
                        checkedBags.append(key)
                        tmpNumber, checkedBags= count_ex_1(bagDict, key, checkedBags)
                        totalNumber += tmpNumber
                        totalNumber += 1
    return totalNumber, checkedBags

def main(filename, test):
    bagDict = {}
    with open(filename) as f:
        if test:
            testResults = f.readline()
            print(testResults)
        for line in f:
            aa = line.rstrip(".\n").split(" bags contain ")
            if aa[1] == "no other bags":
                bagDict[aa[0]] = [""]
            else:
                inside = aa[1].split(", ")
                bagDict[aa[0]] = []
                for bag in inside:
                    bagDict[aa[0]].append(bag)
    bagToCheck = "shiny gold"
    ex1 = count_ex_1(bagDict, bagToCheck)

    print("Our bag can be in", ex1[0], "other bags")








if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Whatever this is going to do")
    parser.add_argument("filename", type = str, help = "The name of the input file")
    parser.add_argument("--test", action="store_true", help="If it is a test, it reads the first line which contains the expected output")


    args = parser.parse_args()
    sys.exit(main(args.filename,args.test))
