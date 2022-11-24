from CFG import *
from CFGtoCNF import *

newCFG = CFG()
newCFG.readCFG('test/tes5.txt')
newCFG.print()
CFGtoCNF(newCFG)
newCFG.print()