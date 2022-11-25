from CFG import *
from CFGtoCNF import *
from Cyk_pharser import *
import re

filename = input("nama file input: ")
with open("test/"+filename,'r') as file:
    fileString = file.read()
fileString = re.sub("\t","",fileString)
fileString = re.sub(" {2,}"," ",fileString)
fileString = re.sub("\n{2,}","\n",fileString)
print(repr(fileString))