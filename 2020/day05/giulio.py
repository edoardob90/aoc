#!/usr/bin/python
import sys
import argparse

def bisect(seatRange,letter):
    if letter == "F" or letter == "L":
        return seatRange[:len(seatRange)//2]
    else:
        return seatRange[len(seatRange)//2:]

def checkSeat(seatString):
    seatRow = range(128)
    for letter in seatString[:-4]:
        seatRow = bisect(seatRow,letter)

    seatColumn = range(8)
    for letter in seatString[-4:]:
        seatColumn = bisect(seatColumn,letter)

    return seatRow[0]*8 + seatColumn[0]
    

def main(filename, test):
    currentSeat = 0
    topSeat = 0
    seatList = []
    with open(filename) as f:
        if test:
            testResults = f.readline()
            print(testResults)
        for line in f:
            currentSeat = checkSeat(line)
            seatList.append(currentSeat)
            if currentSeat > topSeat:
                topSeat = currentSeat

    seatList.sort()
    mySeat = 0
    for idx,seat in enumerate(seatList[1:-2]):
        if not (((seat - 1) == seatList[idx]) and ((seat + 1) == seatList[idx+2])):
            mySeat += seat / 2 

    print("Highest seat ID",topSeat)
    print("My seat is",int(mySeat))





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Whatever this is going to do")
    parser.add_argument("filename", type = str, help = "The name of the input file")
    parser.add_argument("--test", action="store_true", help="If it is a test, it reads the first line which contains the expected output")


    args = parser.parse_args()
    sys.exit(main(args.filename,args.test))
