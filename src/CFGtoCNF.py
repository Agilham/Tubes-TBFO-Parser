from collections import deque
from itertools import *
from CFG import *

def nextAvailable(var,variabel):
    # mencari variabel baru dari list variabel yang ada.
    # produksi variabel dimulai menaikkan char terakhir hingga 'Z', 
    # jika masih ada maka tambah karakter baru, lakukan hingga tidak ada pada set variabel
    while var in variabel:
        if (ord(var[len(var)-1])-ord('A') >= 25):
            var += 'A'
        else:
            var = var[:len(var)-1] + chr(ord(var[len(var)-1])+1)
    return var


def getSoleProductor(product, production):
    # mencari LHS di production yang menghasilkan product saja
    for LHS in production:
        if (len(production[LHS]) != 1):
            continue
        for RHS in production[LHS]:
            if (product == RHS):
                return LHS
    return None

def getCombinationOfNullable(RHS, nullable):
    # mengembalikan set dari kombinasi tuple RHS yang dimana variabel nullable nya boleh dihilangkan
    # (N A N) = {(N A N), (A N), (N A), (A)}
    newProduct = set()
    if (len(RHS) != 0):
        combTail = getCombinationOfNullable(RHS[1:],nullable)
        if RHS[0] in nullable:
            newProduct = newProduct.union(combTail)
        for comb in combTail:
            newProduct.add((RHS[0],)+comb)
    else:
        newProduct.add(tuple())
    return newProduct

def removeUseless(CFG : CFG):
    # menghilangkan produksi yang tidak berguna dari CFG

    # ** menghilangkan produksi yang tidak produktif ** 
    # mencari variabel yang menghasilkan terminal secara langsung
    productiveVar = set()
    for LHS in CFG.produksi:
        for RHS in CFG.produksi[LHS]:
            isAllTerminal = True
            for i in range(len(RHS)):
                if RHS[i] not in CFG.terminal:
                    isAllTerminal = False
            if isAllTerminal:
                productiveVar.add(LHS)
                break
    # menambahkan variabel produktif secara tidak langsung
    n = 0
    while n != len(productiveVar):
        n = len(productiveVar)
        for LHS in CFG.produksi:
            for RHS in CFG.produksi[LHS]:
                isAllTerminal = True
                for i in range(len(RHS)):
                    if (RHS[i] not in CFG.terminal) and (RHS[i] not in productiveVar):
                        isAllTerminal = False
                        break
                if isAllTerminal:
                    productiveVar.add(LHS)
                    break
    # hapus variabel yang tidak produktif beserta produksinya
    for LHS in list(CFG.produksi.keys()):
        tupleTodelete = set()
        for RHS in CFG.produksi[LHS]:
            doDelete = False
            for i in range(len(RHS)-1,-1,-1):
                if RHS[i] not in CFG.terminal and RHS[i] not in productiveVar:
                    doDelete = True
                    break
            if doDelete:
                tupleTodelete.add(RHS)
        CFG.produksi[LHS] -= tupleTodelete
        if CFG.produksi[LHS] == set():
            del CFG.produksi[LHS]

    # ** menghilangkan produksi yang tidak dapat dicapai symbol start ** 
    # mencari variabel yang dapat diakses start
    reachableVar = set({"SS"})
    reachableTerminal = set()
    n_bef = 0
    while n_bef != len(reachableVar)+len(reachableTerminal):
        n_bef = len(reachableVar)+len(reachableTerminal)
        for LHS in CFG.produksi:
            if LHS in reachableVar :
                for RHS in CFG.produksi[LHS]:
                    for i in range(len(RHS)):
                        if (RHS[i] in CFG.terminal):
                            reachableTerminal.add(RHS[i])
                        else:
                            reachableVar.add(RHS[i])
    # menghapus variabel yang tidak dapat diakses start
    for LHS in list(CFG.produksi.keys()):
        if LHS not in reachableVar:
            del CFG.produksi[LHS]
    CFG.terminal = reachableTerminal
    CFG.variabel = reachableVar

def removeEps(CFG:CFG):
    CFG.produksi = CFG.produksi
    nullable = set()
    n_bef = -1
    while (n_bef != len(nullable)):
        n_bef = len(nullable)
        for LHS in list(CFG.produksi.keys()):
            toBeDeleted = set()
            for RHS in CFG.produksi[LHS]:
                if (len(RHS) == 1 and RHS[0] == ""):
                    nullable.add(LHS)
                    toBeDeleted.add(RHS)
                    break
            CFG.produksi[LHS] -= toBeDeleted
            if len(CFG.produksi[LHS]) == 0:
                del CFG.produksi[LHS]
        for LHS in list(CFG.produksi.keys()):
            for RHS in CFG.produksi[LHS]:
                isAllNullable = True
                for i in range(len(RHS)):
                    if (RHS[i] not in nullable):
                        isAllNullable = False
                        break
                if (isAllNullable):
                    nullable.add(LHS)
    for LHS in list(CFG.produksi.keys()):
        toBeAdded = set()
        for RHS in CFG.produksi[LHS]:
            isThereNullable = False
            for i in range(len(RHS)):
                if (RHS[i] in nullable):
                    isThereNullable = True
                    break
            if (isThereNullable):
                comb = getCombinationOfNullable(RHS,nullable)
                comb = filter(None, comb)
                toBeAdded = toBeAdded.union(comb)
        CFG.produksi[LHS] = CFG.produksi[LHS].union(toBeAdded)

def removeUnit(CFG : CFG):
    nonUnit = {}
    unit = {}
    lenUnit = 0
    for LHS in CFG.produksi:
        for RHS in CFG.produksi[LHS]:
            if len(RHS) == 1 and RHS[0] in CFG.variabel:
                if LHS not in unit:
                    unit[LHS] = set()
                unit[LHS].add(RHS[0])
                lenUnit += 1
            else:
                if LHS not in nonUnit:
                    nonUnit[LHS] = set()
                nonUnit[LHS].add(RHS) 
    for t in range(lenUnit):
        for A in unit:
            for B in unit[A]:
                if A != B and B in nonUnit:
                    for B_RHS in nonUnit[B]:
                        if A not in nonUnit:
                            nonUnit[A] = set()
                        nonUnit[A].add(B_RHS)
    CFG.produksi = nonUnit

def simplifyCFG(CFG:CFG):
    removeEps(CFG)
    removeUnit(CFG)
    removeUseless(CFG) 

def CFGtoCNF(CFG : CFG):
    simplifyCFG(CFG)
    for LHS in CFG.produksi:
        CFG.produksi[LHS] = list(CFG.produksi[LHS])
        for i in range(len(CFG.produksi[LHS])):
            CFG.produksi[LHS][i] = list(CFG.produksi[LHS][i])
    newVar = nextAvailable("AA",CFG.variabel)
    for LHS in list(CFG.produksi.keys()):
        for RHS in CFG.produksi[LHS]:
            if (len(RHS) > 1):
                for i in range(len(RHS)):
                    if (RHS[i] in CFG.terminal):
                        productor = getSoleProductor([RHS[i]],CFG.produksi)
                        if productor is None:
                            CFG.produksi[newVar] = [[RHS[i]]]
                            RHS[i] = newVar
                            CFG.variabel.add(newVar)
                            newVar = nextAvailable(newVar,CFG.variabel)
                        else:
                            RHS[i] = productor
    isCNFValid = False
    while (not isCNFValid):
        isCNFValid = True
        for LHS in list(CFG.produksi.keys()):
            for RHS in CFG.produksi[LHS]:
                if (len(RHS) > 2):
                    isCNFValid = False
                    lengthRHS = len(RHS)
                    for i in range(lengthRHS-2,-1,-2):
                        subset = RHS[i:i+2]
                        del RHS[i:i+2]
                        productor = getSoleProductor(subset,CFG.produksi)
                        if productor is None :
                            CFG.produksi[newVar] = [subset]
                            RHS.append(newVar)
                            CFG.variabel.add(newVar)
                            newVar = nextAvailable(newVar,CFG.variabel)
                        else:
                            RHS.append(productor)
    for LHS in CFG.produksi:
        for i in range(len(CFG.produksi[LHS])):
            CFG.produksi[LHS][i] = tuple(CFG.produksi[LHS][i])
        CFG.produksi[LHS] = set(CFG.produksi[LHS])



