from CFG import *
from tqdm import tqdm
def cykPharser(input, cnfGrammar:CFG) : 
    Ni = len(input); 
    cyktab = [[set() for j in range(Ni)] for i in range(Ni+1)]

    for i in range(Ni): 
        for LHS in cnfGrammar.produksi : 
            for product in cnfGrammar.produksi[LHS] : 
                if len(product) == 1 and product[0] == input[i] : 
                    cyktab[1][i].add(LHS)

    for l in tqdm(range(2,Ni+1)) : 
        for i in range(0,Ni-l+1):
            for l1 in range(1,l) : 
                l2 = l-l1
                for LHS in cnfGrammar.produksi : 
                    for product in cnfGrammar.produksi[LHS]: 
                        if len(product)==2 : 
                            if (product[0] in cyktab[l1][i]) and (product[1] in cyktab[l2][i+l1]): 
                                cyktab[l][i].add(LHS)
    if "SS" in cyktab[Ni][0] : 
        print("accepted input!")
    else: 
        print("syntax error! ")