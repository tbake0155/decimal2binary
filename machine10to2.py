#!/usr/bin/env python3
#
# 10to2 will find the base 2 equivalent of a base 10 integer
# using built in functionality
#
# the program will accept an integer as command line argument
# and then output the base 2 equivalent of that number to the user
#
# Author: Timothy Baker
# Date  : September 2017
# Class : CS 517
# Assg  : Machine Assignment 1, Problem 1

import sys

def main() :
    if len(sys.argv) > 1 :
        try :
            userInteger = int(sys.argv[1])
            if type(userInteger) == int :
                print(bin(userInteger)[2:])
            else :         
                print("error: invalid input")
        except :
            print("error: input must be an integer")
    else :
        print("usage error: requires an integer input")

if __name__ == "__main__":
    main()

#end of file 

