#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getopt

def writeToFile(fileOut, contents):
    f = open(fileOut, 'w+')
    f.write(str(contents))
    f.close()
    print ("Finished generating data")


def readFromFile(filein):

    file = open(filein, 'r')
    contents = file.read()
    file.close()
    return contents

def readLineAsArray(filein):
    array = []
    with open(filein, "r") as ins:
        for line in ins:
            array.append(line)

def appendLineToFile(fileout, line):
    with open(fileout, "a") as f:
        f.write(line + "\n")

