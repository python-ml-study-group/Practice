import os
print ("The current working directory is: ", os.getcwd())

from os import getcwd
print ("The current working directory is: ", getcwd())

from os import getcwd as getCurrentWorkingDirectory
print ("The current working directory is: ", getCurrentWorkingDirectory())

from othermodule import add
print(add(2,3   ))

import sys
sys.path.append("C:/Projects/Practice-1")

from Nagasai.abc import add1
print("add1 result: ", add1(2,3))

import common_as
common_as.file_util.getTempfile()
