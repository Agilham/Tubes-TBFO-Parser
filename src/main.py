from CFG import *
from CFGtoCNF import *
from Cyk_parser import *
import re
import sys

if (len(sys.argv) == 2):
    filename = sys.argv[1]
elif (len(sys.argv) == 1):
    filename = input("nama file input: ")
else:
    print("usage: python src/main.py [filename]")
    exit()

with open("test/"+filename,'r') as file:
    fileString = file.read()
fileString = re.sub("\t","",fileString)
fileString = re.sub(" {2,}"," ",fileString)
fileString = re.sub("\n{2,}","\n",fileString)
grammar = CFG()
grammar.readCFG("test/grammar.txt")
CFGtoCNF(grammar)
print("Compiling...")
cykPharser(fileString,grammar)