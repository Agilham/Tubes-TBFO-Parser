def cykPharser(input,cnfGrammar) : 
    Ni = len(input); 
    cyktab = [[set([]) for i in range(Ni)] for j in range(Ni)]

    for i in range(Ni): 
        for variabel in cnfGrammar.items() : 
            for terminal in variabel[1] : 
                if len(terminal) == 1 and terminal[0] == input[i] : 
                    cyktab[i][i].add(variabel[0])

    for s in range(2,Ni+1) : 
        for i in range(0,Ni-s+1) : 
            j = i+s-1
            for z in range(i,j) : 
                for variabel in cnfGrammar.items() : 
                    for product in variabel[1]: 
                        if len(product)==2 : 
                            if (product[0] in cyktab[i][z]) and (product[1] in cyktab[z+1][j]) : 
                                cyktab[i][j].add(variabel[0])
    if "S0" in cyktab[0][Ni-1] : 
        print("accepted input!")
    else: 
        print("syntax error! ")