from CFG import *
from CFGtoCNF import *
from Cyk_pharser import *

newCFG = CFG()
newCFG.readCFG('test/tesCYK.txt')
newCFG.print()
CFGtoCNF(newCFG)
newCFG.print()
cykPharser("ababa",newCFG)