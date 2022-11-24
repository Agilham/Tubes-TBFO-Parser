from CFG import *

def cykPharser(input, cnfGrammar:CFG) : 
    Ni = len(input); 
    cyktab = [[set() for i in range(Ni)] for j in range(Ni)]

    for i in range(Ni): 
        for LHS in cnfGrammar.produksi : 
            for product in cnfGrammar.produksi[LHS] : 
                if len(product) == 1 and product[0] == input[i] : 
                    cyktab[i][i].add(product[0])

    for s in range(2,Ni+1) : 
        for i in range(0,Ni-s+1) : 
            j = i+s-1
            for z in range(i,j) : 
                for LHS in cnfGrammar.produksi : 
                    for product in cnfGrammar.produksi[LHS]: 
                        if len(product)==2 : 
                            if (product[0] in cyktab[i][z]) and (product[1] in cyktab[z+1][j]) : 
                                cyktab[i][j].add(LHS)
    for i in range(Ni):
        for j in range(Ni):
            print(cyktab[i][j],end='')
        print()
    if "SS" in cyktab[0][Ni-1] : 
        print("accepted input!")
    else: 
        print("syntax error! ")