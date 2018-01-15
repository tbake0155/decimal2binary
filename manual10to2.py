#!/usr/bin/env python3
#
# 10to2 will find the base 2 equivalent of a base 10 integer
#
# the program will accept an integer as command line argument
# and then output the base 2 equivalent of that number to the user
#
# Author: Timothy Baker
# Date  : September 2017
# Class : CS 517
# Assg  : Machine Assignment 1, Problem 1

import sys

def findMagnitude(integer) :
    raisedTo = 0
    base = 1
    while base < integer :
         raisedTo = raisedTo + 1
         base = pow(2, raisedTo)
    return raisedTo

def bitStringByByte(bitString) :
    extraBits = 8 - len(bitString) % 8 
    for i in range(0,extraBits) :
        bitString = "0" + bitString
    bitString = list(bitString)
    length = len(bitString) + 1
    i = 1
    solution = 0
    firstTry = True
    while i <= length :
        if i % 8 == 0 :
            bitString.insert(i+solution,' ')
            solution = solution + 1
            length = length + 1
        i = i + 1
    bitString = "".join(bitString)
    return bitString
           
def manBin(integer) :
    remainder = integer
    magnitude = findMagnitude(integer)
    print(magnitude)
    powerDown = magnitude
    bitString = ""
    for i in range (0, magnitude + 1) :
        bitString = "0" + bitString
    bitString = list(bitString)
    while remainder != 0 :
        if remainder - pow(2,powerDown) >= 0 :
            remainder = remainder - pow(2,powerDown)
            bitString[magnitude - powerDown] = '1'
        powerDown = powerDown - 1
    bitString = "".join(bitString)
    bitString = bitStringByByte(bitString)
    return bitString

def main() :
    if len(sys.argv) > 1 :
        if True :
            userInteger = int(sys.argv[1])
            if type(userInteger) == int :
                if userInteger == 0 :
                    print("\nDecimal = 0, Binary = 00000000\n")
                else :
                    print ("\nDecimal =", userInteger, ", Binary =", manBin(userInteger), "\n")
            else :         
                print("error: invalid input")
        else :
            print("error: input must be an integer")
    else :
        print("usage error: requires an integer input")

if __name__ == "__main__":
    main()

#end of file 

