"""Implementing the tac shell command in python."""

import sys
"""lets us access system specific parameters & functions used/maintained by Interpreter"""
from lib.helper import tac, readfile
"""import cat function defined in lib.helper file """

TEXT = None     #TEXT variable is defined as NONE type
ARG_CNT = len(sys.argv) - 1     #ARG_CNT defined as len(sys.argv) minus 1

if ARG_CNT == 0:     #if ARG_CNT equals 0, then execute the following
    TEXT = sys.stdin.read()     #then TEXT variable gets updated to read all the arguments

if ARG_CNT == 1:    #if ARG_CNT equals 1, then execute the following
    filename = sys.argv[1]      #then filename variable is equivalent to sys.argv[1]
    TEXT = readfile(filename)   #then TEXT variable gets updated to readfile with a filename

if ARG_CNT > 1:   #if ARG_CNT is greater than 1, then execute the following  
    print(sys.argv[0], "doesn't handle more than one argument")
    #print with a name of program followed by doesn't handle more than one argument

print(tac(TEXT))    #print the arguments of the file in reverse order
