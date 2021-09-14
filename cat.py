"""Implementing the cat shell command in python."""

import sys
"""lets us access system specific parameters & functions used/maintained by Interpreter"""
from lib.helper import cat, readfile
"""import cat function defined in lib.helper file """

TEXT = None     #TEXT variable is defined as NONE type
ARG_CNT = len(sys.argv) - 1 
#argument count variable takes length(method) of the system arguments minus 1

if ARG_CNT == 0:    #if ARG_CNT=0, execute the following
    TEXT = sys.stdin.read()     #then read the system variable input

if ARG_CNT == 1:    #if ARG_CNT=1, execute the following
    filename = sys.argv[1]  #then sys.argv[1]==filename
    TEXT = readfile(filename)   #TEXT read the arguments with reference to filename

if ARG_CNT > 1:     #if ARG_CNT>1, then execute the following
    print(sys.argv[0], "doesn't handle more than one argument")    
    #print name of program, doesn't handle more than one argument

print(cat(TEXT))    #print TEXT variable based on above conditions

