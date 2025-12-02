#!/usr/bin/python
import sys
import argparse

def addAnyAnswer(currentAnswer):
    squeezeAnswer = []
    for element in currentAnswer:
        squeezeAnswer += element
    return len(set(squeezeAnswer))

def addAllAnswer(currentAnswer):
    allAnswers = 0
    numberOfElements = len(currentAnswer)
    counterAnswers = {}
    for letter in currentAnswer[0]:
        counterAnswers[letter] = 0
        for element in currentAnswer:
            if letter in element:
                counterAnswers[letter] += 1

        if counterAnswers[letter] == numberOfElements:
            allAnswers += 1

    return allAnswers

def main(filename, test):
    currentAnswer = []
    anyCounter = 0
    allCounter = 0
    check = []    
    with open(filename) as f:
        if test:
            testResults = f.readline()
            print(testResults)
        for line in f:
            if line == "\n":
                anyCounter += addAnyAnswer(currentAnswer)
                allCounter += addAllAnswer(currentAnswer)
                currentAnswer = []
                check = []
            else:
#                currentAnswer += line.rstrip()
                currentAnswer.append(line.rstrip())
    anyCounter += addAnyAnswer(currentAnswer)
    allCounter += addAllAnswer(currentAnswer)
    print("The number of answers with at least one yes is", anyCounter)
    print("The number of answers with at all being yes is", allCounter)
                






if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Whatever this is going to do")
    parser.add_argument("filename", type = str, help = "The name of the input file")
    parser.add_argument("--test", action="store_true", help="If it is a test, it reads the first line which contains the expected output")


    args = parser.parse_args()
    sys.exit(main(args.filename,args.test))
