"""Implementing the wc shell command in python."""

import sys
"""lets us access system specific parameters & functions used/maintained by Interpreter"""
from lib.helper import wc, readfile
"""import cat function defined in lib.helper file """

TEXT = None      #TEXT variable is defined as NONE type
ARG_CNT = len(sys.argv) - 1      #ARG_CNT defined as len(sys.argv) minus 1

if ARG_CNT == 0:     #if ARG_CNT equals 0, then execute the following
    TEXT = sys.stdin.read()     #then TEXT variable gets updated to read all the arguments

if ARG_CNT == 1:    #if ARG_CNT equals 1, then execute the following
    filename = sys.argv[1]      #then filename variable is equivalent to sys.argv[1]
    TEXT = readfile(filename)   #then TEXT variable gets updated to readfile with a filename

response = wc(TEXT)     #response variable gets updated with word count of the file
print(" " + str(response[0]) + "  " + str(response[1]) + " " + str(response[2]))
"""prints response[0] with no. of lines, response[1] with no. of words & response[2] with no. of chars
based on the function defination done in lib.helper file"""