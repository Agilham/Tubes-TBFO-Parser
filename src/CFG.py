class CFG:
    produksi = dict()
    variabel = set()
    terminal = set()
    
    def readCFG(self,filepath):
        newProduksi = dict()
        newVariabel = set()
        newTerminal = set()
        with open(filepath) as f:
            list = f.read().splitlines()
        maxRow = len(list)
        for i in range(maxRow):
            maxCol = len(list[i])
            foundKey = False
            foundStart = False
            word = ""
            for j in range(maxCol):
                char = list[i][j]
                if (not(foundKey)):
                    if (char == ' '):
                        foundKey = True
                        key = word
                        newProduksi[key] = set()
                        word = char
                    else:
                        word += char
                elif (not(foundStart)):
                    word += char
                    if (word == " => "):
                        foundStart = True
                        RHS = []
                        word = ""
                else:
                    foundVal = False
                    if (not(foundVal)):
                        if (char != ' ') & (char != '|'):
                            word += char
                        if (char == ' ') | (char == '|') | (j == maxCol-1):
                            foundVal = True
                            val = word
                            word = ""
                    if (foundVal):
                        if (val != ""):
                            if (val == "eps"):
                                val = ""
                            elif (val == "spc"):
                                val = " "
                            RHS.append(val)
                            if (len(val) > 1):
                                newVariabel.add(val)
                            elif (val != ""):
                                newTerminal.add(val)
                            if (j == maxCol-1):
                                newProduksi[key].add(tuple(RHS))
                                RHS = []
                        else:
                            if (char == '|'):
                                newProduksi[key].add(tuple(RHS))
                                RHS = []
            self.produksi = newProduksi
            self.variabel = newVariabel
            self.terminal = newTerminal

    def print(self):
        print("variabel :",self.variabel)
        print("terminal :",self.terminal)
        print("produksi :")
        for LHS in self.produksi:
            print(LHS+ " =>",end="")
            i = 0
            for RHS in self.produksi[LHS]:
                for komponen in RHS:
                    if (len(komponen) == 0):
                        print(" eps",end="")
                    elif (len(komponen) == 1 and komponen[0] == " "):
                        print(" spc",end="")
                    else:
                        print(" " + komponen,end="")
                if (i != len(self.produksi[LHS])-1):
                    print(" |",end="")
                i += 1
            print()
