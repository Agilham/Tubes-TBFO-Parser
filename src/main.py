from CFG import *
from CFGtoCNF import *
from Cyk_parser import *
import re

filename = input("nama file input: ")
with open("test/"+filename,'r') as file:
    fileString = file.read()
fileString = re.sub("\t","",fileString)
fileString = re.sub(" {2,}"," ",fileString)
fileString = re.sub("\n{2,}","\n",fileString)
grammar = CFG()
grammar.readCFG("test/grammar.txt")
grammar.print()
CFGtoCNF(grammar)
cykPharser(fileString,grammar)