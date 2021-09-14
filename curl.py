"""The python code helps to read the command line input for curl method."""

import sys
"""lets us access system specific parameters & functions used/maintained by Interpreter"""
from lib.helper import curl
"""import cat function defined in lib.helper file """

URL = None  #URL variabled efined as NONE type
ARG_CNT = len(sys.argv) - 1 #ARG_CNT defined as len(sys.argv) minus 1

if ARG_CNT != 1:    #if ARG_CNt is not equal to 1, then execute the following
    print('Usage: curl [URL]...')   
    #then print while using curl [URL], all data in the server gets displayed 

if ARG_CNT == 1:    #if ARG_CNT=1, then execute the following
    URL = sys.argv[1]   #URL takes the file name as sys.argv[1]==filename
    if 'http' not in URL[:5]:   
        #if HTTP not in URL[:5] i.e., reads args from 0-4, then execute the following 
        URL = "http://"+URL #then https:// gets added to the value of URL=sys.argv[1]
    print(curl(URL))    #prints all the data from a server
